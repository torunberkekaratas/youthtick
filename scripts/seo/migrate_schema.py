#!/usr/bin/env python3
"""Migrate JS-injected schema.org to static <script type="application/ld+json"> in <head>."""

import re
import json
from pathlib import Path


def extract_js_object(text, start_pos):
    """Extract a JS object starting from start_pos (after 'const schema = ').
    Properly handles string literals (both single- and double-quoted),
    returning (object_text, end_index) or (None, -1) on failure.
    """
    depth = 0
    in_string = False
    string_char = None
    escaped = False
    i = start_pos

    # Skip whitespace / '=' to reach the opening '{'
    while i < len(text) and text[i] != '{':
        i += 1

    if i >= len(text):
        return None, -1

    obj_start = i

    while i < len(text):
        c = text[i]

        if escaped:
            escaped = False
        elif in_string:
            if c == '\\':
                escaped = True
            elif c == string_char:
                in_string = False
        else:
            if c in ('"', "'"):
                in_string = True
                string_char = c
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return text[obj_start:i + 1], i + 1

        i += 1

    return None, -1


def js_obj_to_json(js_text):
    """Convert a JS object literal (single-quoted strings) to valid JSON text."""
    result = []
    i = 0
    n = len(js_text)

    while i < n:
        c = js_text[i]

        if c == "'":
            # Single-quoted string -> double-quoted JSON string
            content = []
            i += 1
            while i < n:
                ch = js_text[i]
                if ch == '\\' and i + 1 < n:
                    nxt = js_text[i + 1]
                    if nxt == "'":
                        content.append("'")   # \' -> ' (unescape)
                        i += 2
                    elif nxt == '"':
                        content.append('\\"')  # \" stays escaped
                        i += 2
                    elif nxt == 'n':
                        content.append('\\n')
                        i += 2
                    elif nxt == 'r':
                        content.append('\\r')
                        i += 2
                    elif nxt == 't':
                        content.append('\\t')
                        i += 2
                    else:
                        content.append('\\')
                        content.append(nxt)
                        i += 2
                elif ch == '"':
                    content.append('\\"')      # bare " inside single-quote -> escape it
                    i += 1
                elif ch == '\n':
                    content.append('\\n')
                    i += 1
                elif ch == '\r':
                    content.append('\\r')
                    i += 1
                elif ch == '\t':
                    content.append('\\t')
                    i += 1
                elif ch == "'":
                    i += 1
                    break
                else:
                    content.append(ch)
                    i += 1
            result.append('"')
            result.extend(content)
            result.append('"')

        elif c == '"':
            # Already double-quoted — pass through verbatim
            result.append(c)
            i += 1
            while i < n:
                ch = js_text[i]
                result.append(ch)
                if ch == '\\' and i + 1 < n:
                    i += 1
                    result.append(js_text[i])
                elif ch == '"':
                    i += 1
                    break
                i += 1

        else:
            result.append(c)
            i += 1

    return ''.join(result)


def migrate_page(filepath):
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')

    # Skip if already has a static ld+json block
    if re.search(r'<script[^>]+type=["\']application/ld\+json["\']', content):
        print(f'  SKIP  {path.name}  (already has static schema)')
        return False

    # Locate the DOMContentLoaded <script> block
    dom_match = re.search(
        r"<script>\s*\ndocument\.addEventListener\('DOMContentLoaded'",
        content
    )
    if not dom_match:
        print(f'  SKIP  {path.name}  (no DOMContentLoaded block)')
        return False

    # Locate 'const schema = ' inside that block
    schema_kw = "const schema = "
    schema_pos = content.find(schema_kw, dom_match.start())
    if schema_pos == -1:
        print(f'  SKIP  {path.name}  (no "const schema =" found)')
        return False

    # Extract the JS object
    js_obj, obj_end = extract_js_object(content, schema_pos + len(schema_kw))
    if js_obj is None:
        print(f'  FAIL  {path.name}  (could not extract schema object)')
        return False

    # Convert JS object notation -> JSON
    json_text = js_obj_to_json(js_obj)

    # Validate JSON
    try:
        parsed = json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f'  FAIL  {path.name}  JSON parse error: {e}')
        # Show the problematic area
        col = e.colno - 1
        snippet = json_text[max(0, col - 60): col + 60]
        print(f'         near: ...{repr(snippet)}...')
        return False

    # Pretty-format
    json_pretty = json.dumps(parsed, ensure_ascii=False, indent=2)

    # Find the full DOMContentLoaded <script>…</script> block to replace
    dom_script_match = re.search(
        r"<script>\s*\ndocument\.addEventListener\('DOMContentLoaded'.*?</script>",
        content, re.DOTALL
    )
    if not dom_script_match:
        print(f'  FAIL  {path.name}  (cannot find closing </script> for DOMContentLoaded)')
        return False

    new_dom_block = (
        "<script>\n"
        "document.addEventListener('DOMContentLoaded', () => {\n"
        "  if (window.lucide) lucide.createIcons();\n"
        "});\n"
        "</script>"
    )

    static_schema_block = (
        f'<script type="application/ld+json">\n{json_pretty}\n</script>\n'
    )

    # Replace DOMContentLoaded block
    new_content = content.replace(dom_script_match.group(0), new_dom_block, 1)

    # Insert static schema before </head>
    head_end = new_content.rfind('</head>')
    if head_end == -1:
        print(f'  FAIL  {path.name}  (no </head> tag)')
        return False

    new_content = new_content[:head_end] + static_schema_block + new_content[head_end:]

    path.write_text(new_content, encoding='utf-8')
    print(f'  OK    {path.name}')
    return True


PAGES = [
    'yalova-dil-okulu.html',
    'yalova-egitim.html',
    'yalova-erasmus-istatistik.html',
    'yalova-esc-gonullu.html',
    'yalova-genclik-toplulugu.html',
    'yalova-gsb.html',
    'yalova-ogrenci-yasami.html',
    'yalova-sivil-toplum.html',
    'yalova-sks.html',
    'yalova-t3.html',
    'yalova-teknofest.html',
    'yalova-teknopark.html',
    'yalova-universite.html',
    'yalova-ytso.html',
]

if __name__ == '__main__':
    base = Path('/home/user/youthtick')
    ok = fail = skip = 0
    for page in PAGES:
        fp = base / page
        if not fp.exists():
            print(f'  MISSING  {page}')
            fail += 1
            continue
        result = migrate_page(fp)
        if result is True:
            ok += 1
        elif result is False:
            # check if it was a skip or fail based on output (we just count both)
            skip += 1

    print(f'\nDone: {ok} migrated, {skip} skipped/failed')

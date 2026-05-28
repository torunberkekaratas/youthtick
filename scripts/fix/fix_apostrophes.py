#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix single-quoted strings containing apostrophes - line by line approach
"""
import re

# Read the file
with open('assets/js/data/articles_clean.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
count = 0

for i, line in enumerate(lines, 1):
    #Pattern: property: 'string with apostrophe',
    # Look for: word: 'text' but text contains '
    # More conservative: only match if line has exactly one pair of single quotes around apostrophe-containing text
    
    # Match patterns like: property: 'text with ' more text',
    match = re.search(r"^(\s*\w+:\s*)'([^']+('[^']+)+)',?\s*$", line)
    
    if match:
        indent = match.group(1)
        string_content = match.group(2)
        # Replace the single quotes around this string with double quotes
        new_line = line.replace(f"'{string_content}'", f'"{string_content}"')
        fixed_lines.append(new_line)
        count += 1
        if count <= 20:
            print(f"  Line {i}: Fixed apostrophe in: {indent[:20]}...")
    else:
        fixed_lines.append(line)

# Write back
with open('assets/js/data/articles.js', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print(f"\n✅ Fixed {count} lines with apostrophe issues!")

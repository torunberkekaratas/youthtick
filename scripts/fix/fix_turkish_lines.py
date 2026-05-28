#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix specific Turkish lines with apostrophes
"""

with open('assets/js/data/articles.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Specific lines to fix (0-indexed)
fixes = {
    4181: lambda line: line.replace("title_tr: 'Yalova'da", "title_tr: \"Yalova'da"),
    4193: lambda line: line.replace("excerpt: 'Yalova'da", "excerpt: \"Yalova'da"),
    4196: lambda line: line.replace("{ q: 'Yalova'da", "{ q: \"Yalova'da"),
    4277: lambda line: line.replace("seoDesc_tr: 'Yalova'da", "seoDesc_tr: \"Yalova'da"),
    4325: lambda line: line.replace("seoDesc_tr: 'Yalova'da", "seoDesc_tr: \"Yalova'da"),
    4343: lambda line: line.replace("title_tr: 'Yalova'da", "title_tr: \"Yalova'da"),
    4349: lambda line: line.replace("seoDesc_tr: 'Yalova'da", "seoDesc_tr: \"Yalova'da"),
    4367: lambda line: line.replace("title_tr: 'Yalova'da", "title_tr: \"Yalova'da"),
}

fixed_count = 0
for line_num, fix_func in fixes.items():
    if line_num < len(lines):
        old_line = lines[line_num]
        lines[line_num] = fix_func(old_line)
        if lines[line_num] != old_line:
            fixed_count += 1
            print(f"  ✓ Fixed line {line_num + 1}")

with open('assets/js/data/articles.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\n✅ Fixed {fixed_count} Turkish apostrophe lines!")

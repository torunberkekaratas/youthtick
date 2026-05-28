#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Targeted fix: Only fix object property values (not template literal content)
"""

with open('assets/js/data/articles.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Replace specific patterns where single quotes wrap strings with apostrophes
# Only for object properties (not backtick template literals)

replacements = [
    # Pattern: property: 'text with apostrophe',
    # Find seoDesc_tr lines
    ("seoDesc_tr: 'Yalova'dan", 'seoDesc_tr: "Yalova\'dan"'),
    ("q: 'Yalova'dan", 'q: "Yalova\'dan"'),
    ("q: 'Portföy nasıl oluşturulur?', a: 'Gerçek projeleri çözün: yerel işletmelere ücretsiz dijital destek, kişisel blog, GitHub'da", 
     'q: "Portföy nasıl oluşturulur?", a: "Gerçek projeleri çözün: yerel işletmelere ücretsiz dijital destek, kişisel blog, GitHub\'da"'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"  ✓ Fixed: {old[:50]}...")

with open('assets/js/data/articles.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed {count} specific patterns!")

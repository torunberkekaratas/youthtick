import os
import glob
import re

html_files = glob.glob('/Users/torunkaratas/Desktop/dernekkk/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old scripts
    content = re.sub(r'<script\s+src="components\.js".*?></script>\n?', '', content)
    content = re.sub(r'<script\s+src="i18n\.js".*?></script>\n?', '', content)
    content = re.sub(r'<script\s+src="articles\.js".*?></script>\n?', '', content)
    content = re.sub(r'<script\s+src="content-bridge\.js".*?></script>\n?', '', content)

    # Remove inline renderNav and renderFooter blocks
    content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*\(\)\s*=>\s*\{\s*renderNav\(.*?\);\s*\}\);\s*</script>', '', content)
    content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*\(\)\s*=>\s*\{\s*renderNav\(.*?\);\s*(renderFooter\(\);\s*)?\}\);\s*</script>', '', content)
    
    # Catch any remaining ones loosely
    content = re.sub(r'<script>\s*document\.addEventListener.*?renderNav.*?</script>', '', content, flags=re.DOTALL)
    
    # Check if app.js is there
    app_script = '<script type="module" src="assets/js/core/app.js"></script>\n'
    if 'assets/js/core/app.js' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{app_script}</body>')
        else:
            content += app_script

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files (removed inline nav/footer calls)")

#!/usr/bin/env python3
import sys
import re
from AppKit import NSPasteboard, NSPasteboardItem

md_file = sys.argv[1]
with open(md_file, 'r') as f:
    content = f.read()

# Strip frontmatter
content = re.sub(r'^---[\s\S]*?---\n', '', content).strip()

# Strip HTML comments (CLAUDE REVIEW blocks)
content = re.sub(r'<!--[\s\S]*?-->', '', content).strip()

# Convert markdown to HTML
lines = content.split('\n')
html_lines = []
for line in lines:
    if line.startswith('## '):
        html_lines.append(f'<h2>{line[3:]}</h2>')
    elif line.startswith('# '):
        html_lines.append(f'<h1>{line[2:]}</h1>')
    elif line.strip() == '':
        html_lines.append('')
    else:
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', line)
        html_lines.append(f'<p>{line}</p>')

html = '\n'.join(html_lines)

pb = NSPasteboard.generalPasteboard()
pb.clearContents()
item = NSPasteboardItem.new()
item.setString_forType_(html, 'public.html')
pb.writeObjects_([item])
print(f"Gekopieerd: {md_file}")

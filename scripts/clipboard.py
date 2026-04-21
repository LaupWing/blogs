#!/usr/bin/env python3
import sys
from AppKit import NSPasteboard, NSPasteboardItem

html_file = sys.argv[1]
with open(html_file, 'r') as f:
    html = f.read()

pb = NSPasteboard.generalPasteboard()
pb.clearContents()
item = NSPasteboardItem.new()
item.setString_forType_(html, 'public.html')
pb.writeObjects_([item])
print(f"Gekopieerd: {html_file}")

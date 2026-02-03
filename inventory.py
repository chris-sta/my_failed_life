import json
import os
import re

JSON_FILE = "index.json"
INVENTORY_FILE = "inventory.html"

with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

files = []
for item in data:
    if isinstance(item, str):
        files.append(item)
    elif isinstance(item, dict):
        files.append(item.get("file") or item.get("filename"))

paths = []
for f in files:
    if os.path.exists(f):
        paths.append(f)
    else:
        print(f"Warning: {f} not found, skipping")

buttons_html = '<div class="inventory-buttons">\n'
for index, path in enumerate(paths, start=1):
    label = f"{index:02}"
    buttons_html += f'  <button onclick="goTo(\'{path}\')">{label}</button>\n'
buttons_html += '</div>'

with open(INVENTORY_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

new_html_content = re.sub(
    r'<div class="inventory-buttons">.*?</div>',
    buttons_html,
    html_content,
    flags=re.DOTALL
)

with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
    f.write(new_html_content)

print(f"inventory.html updated!")

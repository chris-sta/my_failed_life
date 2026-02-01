import json
import os
import re

JSON_FILE = "index.json"
MARKER = "<!-- PAGE_COUNTER -->"
CSS_LINK = '<link rel="stylesheet" href="../styles/counter.css">'

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
    full_path = f
    if os.path.exists(full_path):
        paths.append(full_path)
    else:
        print(f"Warning: {full_path} not found, skipping")

total = len(paths)
print(f"Found {total} pages")

counter_re = re.compile(r'<div class="page-counter">.*?</div>', re.DOTALL)

for index, path in enumerate(paths, start=1):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = counter_re.sub("", content)

    if CSS_LINK not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"    {CSS_LINK}\n</head>")
        else:
            content = CSS_LINK + "\n" + content

    counter_html = f'<div class="page-counter">{index}/{total}</div>'
    if MARKER in content:
        content = content.replace(MARKER, counter_html)
    else:
        if "</body>" in content:
            content = content.replace("</body>", counter_html + "\n</body>")
        else:
            content += counter_html

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("COMPLETE ✅")
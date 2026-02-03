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
    if os.path.exists(f):
        paths.append(f)
    else:
        print(f"Warning: {f} not found, skipping")

total = len(paths)
print(f"Found {total} pages")

nav_re = re.compile(
    r'\n*\s*<div class="page-counter">.*?</div>\s*<div class="page-buttons">.*?</div>\s*\n*',
    re.DOTALL
)

for index, path in enumerate(paths, start=1):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = nav_re.sub("\n", content)

    if CSS_LINK not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"    {CSS_LINK}\n</head>")
        else:
            content = CSS_LINK + "\n" + content

    navigation_html = f"""
<div class="page-counter">{index}/{total}</div>
<div class="page-buttons">
    <button onclick="location.href='https://chris-sta.github.io/my_failed_life/index.html'">
        Home
    </button>
    <button onclick="location.href='https://chris-sta.github.io/my_failed_life/inventory.html'">
        Inventory
    </button>
</div>
"""

    if MARKER in content:
        content = content.replace(MARKER, navigation_html.strip())
    else:
        if "</body>" in content:
            content = content.replace("</body>", navigation_html + "\n</body>")
        else:
            content += navigation_html

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
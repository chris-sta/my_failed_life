import json

with open("index.json", "r") as f:
    files = json.load(f)

link_lines = []
for file_path in files:
    name = file_path.split("/")[-1].replace(".html", "")
    line = f'<a href="{file_path}" target="_blank">{name}</a><br>'
    link_lines.append(line)

with open("hiventory.html", "w") as f:
    f.write("\n".join(link_lines))

print("hiventory.html updated!")

import os
import json

BASE_DIR = "creations"
OUTPUT_FILE = "index.json"

output = []
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        path = os.path.join(root, file)
        output.append(path.replace("\\", "/"))  # normalize Windows paths

output.sort(key=lambda s: s.lower())

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)

print(f"Indexed {len(output)} files into {OUTPUT_FILE}.")

import subprocess
import time
import sys

subprocess.run(["python", "python/index_creations.py"])

wait_seconds = 10
for i in range(wait_seconds, 0, -1):
    sys.stdout.write(f"\rWaiting {i} seconds... ")
    sys.stdout.flush()
    time.sleep(1)
print("\n")

subprocess.run(["python", "python/number_from_json.py"])

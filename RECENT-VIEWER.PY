import os
import time

#===============================
AUTHOR = "BLACK-HAT_NS"
SCAN_PATH = "/storage/emulated/0"
#================================

print("=" * 65)
print(" ANDROID RECENT FILE ACTIVITY ")
print(f" Created by : {AUTHOR}")
print("=" * 65)

files = []

for root, dirs, filenames in os.walk(SCAN_PATH):
    for name in filenames:
        try:
            full_path = os.path.join(root, name)
            stat = os.stat(full_path)
            files.append((full_path, stat.st_mtime))
        except:
            pass

files.sort(key=lambda x: x[1], reverse=True)

for i, f in enumerate(files[:25], 1):
    print(f"[{i:02}] {f[0]}")
    print(f"     Modified : {time.ctime(f[1])}")
    print("-" * 60)

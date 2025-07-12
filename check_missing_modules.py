import os, json

QUEUE_PATH = "autonomy/module_queue.json"
ROOT = "hedge_fund_ai_package"

with open(QUEUE_PATH) as f:
    queue = json.load(f)

missing = []
for path in queue.keys():
    full_path = os.path.join(ROOT, path.replace("hedge_fund_ai_package/", ""))
    if not os.path.exists(full_path):
        missing.append(path)

print(f"✅ {len(queue) - len(missing)} modules found.")
print(f"❌ {len(missing)} modules missing.")
if missing:
    print("\nMissing modules:")
    for m in missing:
        print("-", m)
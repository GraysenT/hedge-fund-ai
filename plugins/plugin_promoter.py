import json
import os
import shutil

LOG_PATH = "plugins/plugin_log.json"
CORE_PATH = "core_strategies"

def promote_winners(threshold=0.9):
    os.makedirs(CORE_PATH, exist_ok=True)
    with open(LOG_PATH) as f:
        logs = json.load(f)

    for name, entry in logs.items():
        if entry.get("private") and not entry.get("error") and "BUY" in str(entry.get("result", "")):
            print(f"🏁 Promoting {name} to core.")
            shutil.copy(f"plugins/{name}.py", f"{CORE_PATH}/{name}.py")

if __name__ == "__main__":
    promote_winners()
    
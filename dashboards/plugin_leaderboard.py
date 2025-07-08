import json
import os
import pandas as pd
from datetime import datetime

LOG_PATH = "plugins/plugin_log.json"

if not os.path.exists(LOG_PATH):
    print("❌ No plugin logs.")
    exit()

with open(LOG_PATH) as f:
    logs = json.load(f)

records = []
for name, log in logs.items():
    records.append({
        "Plugin": name,
        "Last Run": log.get("last_run"),
        "Result": log.get("result", ""),
        "Errors": log.get("error", "None")
    })

df = pd.DataFrame(records)
df["Last Run"] = pd.to_datetime(df["Last Run"])
df = df.sort_values(by="Last Run", ascending=False)

print("\n🏁 Plugin Leaderboard:\n")
print(df.to_string(index=False))

import os
import json
import pandas as pd

PERF_PATH = "memory/performance"

# Load latest performance
if not os.path.exists(PERF_PATH):
    print("❌ No performance logs found.")
    exit()

latest_file = sorted(os.listdir(PERF_PATH))[-1]
with open(os.path.join(PERF_PATH, latest_file)) as f:
    perf = json.load(f)

records = []
for strat, result in perf.items():
    records.append({
        "Strategy": strat,
        "Capital": result["capital_allocated"],
        "Return %": round(result["return_pct"] * 100, 2),
        "PnL ($)": result["pnl"]
    })

df = pd.DataFrame(records).sort_values(by="PnL ($)", ascending=False)
print(f"\n📊 Daily Strategy Performance ({latest_file}):\n")
print(df.to_string(index=False))

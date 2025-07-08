import os
import json
import pandas as pd

PERF_PATH = "memory/performance"
cumulative = {}

# Read all performance files
for file in sorted(os.listdir(PERF_PATH)):
    with open(os.path.join(PERF_PATH, file)) as f:
        daily = json.load(f)
        for strat, res in daily.items():
            if strat not in cumulative:
                cumulative[strat] = {
                    "Total PnL": 0.0,
                    "Days Traded": 0
                }
            cumulative[strat]["Total PnL"] += res["pnl"]
            cumulative[strat]["Days Traded"] += 1

# Format as DataFrame
df = pd.DataFrame([
    {
        "Strategy": strat,
        "Total PnL": round(info["Total PnL"], 2),
        "Days Traded": info["Days Traded"],
        "Avg Daily PnL": round(info["Total PnL"] / info["Days Traded"], 2)
    }
    for strat, info in cumulative.items()
]).sort_values(by="Total PnL", ascending=False)

print("\n📈 Cumulative Strategy Performance:\n")
print(df.to_string(index=False))

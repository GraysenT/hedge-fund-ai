import json
import os
import pandas as pd

with open("strategy_memory/strategy_lineage.json") as f:
    lineage = json.load(f)

with open("memory/performance/" + sorted(os.listdir("memory/performance"))[-1]) as f:
    perf = json.load(f)

records = []
for strat, info in lineage.items():
    records.append({
        "Strategy": strat,
        "Parent": info.get("parent", "root"),
        "Depth": info.get("depth", 0),
        "Sharpe": info.get("sharpe", 0),
        "Rating": info.get("rating", "N/A"),
        "Latest PnL": perf.get(strat, {}).get("pnl", 0)
    })

df = pd.DataFrame(records)
df = df.sort_values(by="Latest PnL", ascending=False)

print("🧬 Strategy Mutation Tracker:\n")
print(df.to_string(index=False))

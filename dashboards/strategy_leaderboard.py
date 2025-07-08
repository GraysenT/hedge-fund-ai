import os
import json
import pandas as pd
from dashboards.alpha_monitor import pivot

PERF_PATH = "memory/performance"
lineage_path = "strategy_memory/strategy_lineage.json"
alpha_scores = pivot.rolling(window=5).mean().dropna().mean().to_dict()

# Build cumulative pnl + survival
records = {}
for file in sorted(os.listdir(PERF_PATH)):
    with open(os.path.join(PERF_PATH, file)) as f:
        perf = json.load(f)
        for strat, res in perf.items():
            if strat not in records:
                records[strat] = {"pnl": 0, "days": 0}
            records[strat]["pnl"] += res["pnl"]
            records[strat]["days"] += 1

with open(lineage_path) as f:
    lineage = json.load(f)

rows = []
for strat, info in records.items():
    rows.append({
        "Strategy": strat,
        "Cumulative PnL": round(info["pnl"], 2),
        "Days Alive": info["days"],
        "Alpha Score": round(alpha_scores.get(strat, 0), 4),
        "Depth": lineage.get(strat, {}).get("depth", 0)
    })

df = pd.DataFrame(rows)
df = df.sort_values(by="Cumulative PnL", ascending=False)

print("\n🏆 Strategy Leaderboard:\n")
print(df.to_string(index=False))

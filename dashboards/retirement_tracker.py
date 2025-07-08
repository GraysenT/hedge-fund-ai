import os
import json
import pandas as pd
from dashboards.alpha_monitor import pivot

PERF_PATH = "memory/performance"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

# Alpha scores
alpha_scores = pivot.rolling(window=5).mean().dropna().mean().to_dict()

# Load lineage
with open(LINEAGE_PATH) as f:
    lineage = json.load(f)

# Strategy survival
survival = {}
for file in sorted(os.listdir(PERF_PATH)):
    with open(os.path.join(PERF_PATH, file)) as f:
        perf = json.load(f)
        for strat, result in perf.items():
            if strat not in survival:
                survival[strat] = {"pnl": 0, "days": 0}
            survival[strat]["pnl"] += result["pnl"]
            survival[strat]["days"] += 1

records = []
for strat, info in survival.items():
    alpha = alpha_scores.get(strat, -1)
    dead = alpha < 0 and info["days"] >= 5
    records.append({
        "Strategy": strat,
        "Total PnL": round(info["pnl"], 2),
        "Days Alive": info["days"],
        "Alpha Score": round(alpha, 4),
        "Depth": lineage.get(strat, {}).get("depth", 0),
        "Retire?": "🪦 YES" if dead else "✅ Keep"
    })

df = pd.DataFrame(records)
df = df.sort_values(by="Retire?", ascending=False)

print("\n📉 Retirement Tracker:\n")
print(df.to_string(index=False))

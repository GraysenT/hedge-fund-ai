import os
import json
import pandas as pd

PERF_PATH = "memory/performance"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

# Build per-strategy history
records = []
for file in sorted(os.listdir(PERF_PATH)):
    with open(os.path.join(PERF_PATH, file)) as f:
        day = json.load(f)
        date = file.replace(".json", "")
        for strat, res in day.items():
            records.append({
                "Strategy": strat,
                "Date": date,
                "PnL": res["pnl"],
                "Return": res["return_pct"]
            })

df = pd.DataFrame(records)

# Calculate Sharpe-like signal decay
pivot = df.pivot(index="Date", columns="Strategy", values="Return").fillna(0)
rolling = pivot.rolling(window=5).mean().dropna()
health = rolling.mean().sort_values(ascending=False)

print("📉 Alpha Health (Last 5-Day Avg Return):\n")
for strat, score in health.items():
    status = "✅" if score > 0 else "❌"
    print(f"{status} {strat} → {round(score * 100, 2)}%")

import pandas as pd
import json
import os

PERF_PATH = "memory/performance"
files = sorted(os.listdir(PERF_PATH))[-10:]  # last 10 days

records = []
for file in files:
    with open(os.path.join(PERF_PATH, file)) as f:
        daily = json.load(f)
        date = file.replace(".json", "")
        for strat, res in daily.items():
            records.append({
                "Date": date,
                "Strategy": strat,
                "Return": res["return_pct"]
            })

df = pd.DataFrame(records)
pivot = df.pivot(index="Date", columns="Strategy", values="Return").fillna(0)

cor_matrix = pivot.corr()
print("\n📉 Strategy Correlation Matrix (Last 10 Days):\n")
print(cor_matrix.to_string())

high_corr = cor_matrix[(cor_matrix > 0.9) & (cor_matrix < 1.0)]
if high_corr.any().any():
    print("\n⚠️ High Correlation Detected — Consider Hedging:")
    print(high_corr.dropna(how='all').dropna(axis=1, how='all'))
else:
    print("\n✅ No hedge required. Strategy set is diversified.")

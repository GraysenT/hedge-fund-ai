import json
import os
import pandas as pd

PERF_PATH = "memory/performance"
files = sorted(os.listdir(PERF_PATH))[-10:]

records = {}
for f in files:
    daily = json.load(open(os.path.join(PERF_PATH, f)))
    for strat, r in daily.items():
        if strat not in records:
            records[strat] = []
        records[strat].append(r["return_pct"])

score = {k: round(pd.Series(v).mean(), 4) for k, v in records.items()}
ranked = sorted(score.items(), key=lambda x: x[1], reverse=True)

print("📈 Alpha Monitor Live Score:")
for strat, s in ranked:
    print(f"{strat}: {s * 100:.2f}% return avg")
    
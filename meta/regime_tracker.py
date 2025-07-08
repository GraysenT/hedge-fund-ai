import os
import json
import pandas as pd
from sklearn.cluster import KMeans

PERF_PATH = "memory/performance"

# Build feature set from daily returns
files = sorted(os.listdir(PERF_PATH))[-30:]
X = []

for file in files:
    with open(os.path.join(PERF_PATH, file)) as f:
        daily = json.load(f)
        row = [v["return_pct"] for v in daily.values()]
        X.append(row)

# Cluster into regimes
model = KMeans(n_clusters=3, random_state=0)
labels = model.fit_predict(X)

# Save regime labels by date
regime_map = dict(zip(files, labels))
with open("meta/market_regimes.json", "w") as f:
    json.dump(regime_map, f, indent=2)

print("🧠 Regime labels saved to meta/market_regimes.json")

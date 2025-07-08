import json
import pandas as pd
import os

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

if not os.path.exists(LINEAGE_PATH):
    print("❌ No lineage file found.")
    exit()

with open(LINEAGE_PATH, "r") as f:
    lineage = json.load(f)

df = pd.DataFrame([
    {
        "Strategy": s,
        "Parent": info.get("parent", "—"),
        "Depth": info.get("depth", "—"),
        "Sharpe": info.get("sharpe", "—"),
        "Rating": info.get("rating", "—"),
    }
    for s, info in lineage.items()
])

df = df.sort_values(by=["Depth", "Sharpe"], ascending=[True, False])
print("📊 Strategy Lineage Tree:\n")
print(df.to_string(index=False))

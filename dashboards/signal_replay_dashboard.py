import json
import os
import pandas as pd

path = "backtest/results/replay_summary.json"
if not os.path.exists(path):
    print("❌ No replay summary found.")
    exit()

with open(path, "r") as f:
    replay = json.load(f)

df = pd.DataFrame([
    {
        "Strategy": strat,
        "Signals Replayed": r["Signals Replayed"],
        "Total Return": r["Total Return"],
        "Avg Return": r["Avg Return"]
    } for strat, r in replay.items()
])

df = df.sort_values(by="Total Return", ascending=False)
print("\n🔁 Signal Replay Accuracy:\n")
print(df.to_string(index=False))

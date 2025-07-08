import json
import os
import pandas as pd

TOURNAMENT_PATH = "agents/agent_tournament_results.json"

with open(TOURNAMENT_PATH) as f:
    results = json.load(f)

df = pd.DataFrame([
    {
        "Agent": agent,
        "PnL": round(info["pnl"], 2),
        "Days Traded": info["days"],
        "Strategies": len(info["strategies"]),
        "Avg PnL/Day": round(info["pnl"]/info["days"], 2) if info["days"] else 0
    }
    for agent, info in results.items()
])

df = df.sort_values(by="PnL", ascending=False)
print("\n🏆 Agent Leaderboard:\n")
print(df.to_string(index=False))

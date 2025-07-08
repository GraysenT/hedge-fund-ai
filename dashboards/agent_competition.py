import json
import os
import pandas as pd

with open("agents/agent_tournament_results.json") as f:
    results = json.load(f)

rows = []
for agent, data in results.items():
    rows.append({
        "Agent": agent,
        "Total PnL": round(data["pnl"], 2),
        "Days": data["days"],
        "Strategies": len(data["strategies"]),
        "Avg/Day": round(data["pnl"] / max(1, data["days"]), 2),
        "Tier": "🔺 Promoted" if data["pnl"] > 0 else "⬇️ Under Review"
    })

df = pd.DataFrame(rows).sort_values(by="Total PnL", ascending=False)

print("\n🤖 Agent Co-opetition Dashboard:\n")
print(df.to_string(index=False))

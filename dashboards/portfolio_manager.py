import json
import os
import pandas as pd

AGENTS_PATH = "agents/agent_registry.json"
TOURNAMENT_PATH = "agents/agent_tournament_results.json"

with open(AGENTS_PATH) as f:
    agent_map = json.load(f)

with open(TOURNAMENT_PATH) as f:
    results = json.load(f)

data = []
for agent, strategies in agent_map.items():
    perf = results.get(agent, {})
    data.append({
        "Agent": agent,
        "Strategies": len(strategies),
        "Last PnL": round(perf.get("pnl", 0), 2),
        "Days": perf.get("days", 0),
        "Tier": "Promoted" if perf.get("pnl", 0) > 0 else "Under Review"
    })

df = pd.DataFrame(data)
df = df.sort_values(by="Last PnL", ascending=False)

print("\n💼 Portfolio Manager Overview:\n")
print(df.to_string(index=False))

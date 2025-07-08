import json
import os

AGENT_PATH = "agents/agent_registry.json"
TOURNAMENT_PATH = "agents/agent_tournament_results.json"

def retire_failed_agents(threshold=-500):
    with open(AGENT_PATH) as f:
        agents = json.load(f)

    with open(TOURNAMENT_PATH) as f:
        results = json.load(f)

    retired = []
    for agent, stats in results.items():
        if stats["pnl"] < threshold:
            print(f"☠️ Retiring agent {agent} (PnL=${round(stats['pnl'], 2)})")
            retired.append(agent)

    for agent in retired:
        agents.pop(agent, None)

    with open(AGENT_PATH, "w") as f:
        json.dump(agents, f, indent=2)

    print(f"\n🪦 Retired {len(retired)} agents.")

if __name__ == "__main__":
    retire_failed_agents()
    
import json
import os
import random
from multi_agent.agent_pool import load_agents

def compete_and_score_agents():
    agents = load_agents()
    scored = []
    for agent in agents:
        pnl = random.uniform(-0.1, 0.3) * agent["capital"]
        agent["pnl"] += pnl
        scored.append({"id": agent["id"], "pnl": agent["pnl"]})
        with open(f"memory/agents/{agent['id']}.json", "w") as f:
            json.dump(agent, f, indent=2)
    print("🏁 Agents scored:")
    for a in scored:
        print(f" - {a['id']}: PnL = {round(a['pnl'], 2)}")
    return scored

if __name__ == "__main__":
    compete_and_score_agents()
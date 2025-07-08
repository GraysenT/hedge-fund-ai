import json
import os
import random
from datetime import datetime

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
TOURNAMENT_PATH = "agents/agent_tournament_results.json"

def load_lineage():
    with open(LINEAGE_PATH) as f:
        return json.load(f)

def load_top_agents():
    with open(TOURNAMENT_PATH) as f:
        data = json.load(f)
    return sorted(data.items(), key=lambda x: x[1]["pnl"], reverse=True)[:2]

def propose_strategy(agent, strat_pool, lineage):
    parent = random.choice(strat_pool)
    proposal_id = f"{agent}_proposal_{random.randint(1000, 9999)}"
    lineage[proposal_id] = {
        "parent": parent,
        "depth": lineage.get(parent, {}).get("depth", 0) + 1,
        "sharpe": 0,
        "rating": "🔬 Proposed",
        "proposed_by": agent,
        "created": datetime.now().isoformat()
    }
    print(f"🧠 {agent} proposed new strategy: {proposal_id}")
    return proposal_id

def run():
    with open(LINEAGE_PATH) as f:
        lineage = json.load(f)
    top_agents = load_top_agents()
    for agent, info in top_agents:
        if info["strategies"]:
            propose_strategy(agent, info["strategies"], lineage)
    with open(LINEAGE_PATH, "w") as f:
        json.dump(lineage, f, indent=2)

if __name__ == "__main__":
    run()
    
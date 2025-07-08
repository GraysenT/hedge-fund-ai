import json
import os
import random

TOURNAMENT_PATH = "agents/agent_tournament_results.json"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def load_results():
    with open(TOURNAMENT_PATH) as f:
        return json.load(f)

def load_lineage():
    with open(LINEAGE_PATH) as f:
        return json.load(f)

def mutate_from_top_agents(agent_results, lineage):
    top = sorted(agent_results.items(), key=lambda x: x[1]["pnl"], reverse=True)[:2]
    parents = []

    for agent, info in top:
        if info["strategies"]:
            strat = random.choice(info["strategies"])
            parents.append(strat)

    if len(parents) < 2:
        print("❌ Not enough parents to mutate.")
        return

    child = f"agent_hybrid_{random.randint(1000,9999)}"
    lineage[child] = {
        "parent": f"{parents[0]}+{parents[1]}",
        "depth": max(lineage.get(parents[0], {}).get("depth", 0), lineage.get(parents[1], {}).get("depth", 0)) + 1,
        "sharpe": 0,
        "rating": "🧬 Hybrid"
    }

    with open(LINEAGE_PATH, "w") as f:
        json.dump(lineage, f, indent=2)

    print(f"🧬 Created hybrid agent strategy: {child} from {parents}")

if __name__ == "__main__":
    results = load_results()
    lineage = load_lineage()
    mutate_from_top_agents(results, lineage)
    
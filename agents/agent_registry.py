import json
import os
from datetime import datetime

AGENT_PATH = "agents/agent_registry.json"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

# Default virtual agent groups (can be expanded)
AGENT_DEFINITIONS = {
    "momentum_alpha": [],
    "macro_rotation": [],
    "short_volatility": [],
    "long_term_trend": []
}

def load_lineage():
    with open(LINEAGE_PATH) as f:
        return json.load(f)

def assign_strategies_to_agents(lineage):
    agent_map = AGENT_DEFINITIONS.copy()
    for strat, info in lineage.items():
        depth = info.get("depth", 0)
        rating = info.get("rating", "")

        # Group based on rating + depth (simplified rules)
        if "Good" in rating or depth >= 3:
            agent_map["momentum_alpha"].append(strat)
        elif depth == 0:
            agent_map["macro_rotation"].append(strat)
        elif "Poor" in rating:
            agent_map["short_volatility"].append(strat)
        else:
            agent_map["long_term_trend"].append(strat)

    return agent_map

def save_agent_registry(agent_map):
    os.makedirs("agents", exist_ok=True)
    with open(AGENT_PATH, "w") as f:
        json.dump(agent_map, f, indent=2)
    print(f"✅ Saved agent registry to {AGENT_PATH}")

if __name__ == "__main__":
    print("🤖 Building Agent Registry...")
    lineage = load_lineage()
    agents = assign_strategies_to_agents(lineage)
    save_agent_registry(agents)
    
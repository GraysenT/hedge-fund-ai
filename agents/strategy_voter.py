import json
import random
import os

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
AGENTS_PATH = "agents/agent_registry.json"
VOTES_PATH = "strategy_memory/strategy_votes.json"

def simulate_vote():
    with open(LINEAGE_PATH) as f:
        lineage = json.load(f)
    with open(AGENTS_PATH) as f:
        agents = json.load(f)

    votes = {}
    for agent, strats in agents.items():
        for strat in lineage:
            if "proposal" in strat or "auto" in strat:
                if strat not in votes:
                    votes[strat] = {"up": 0, "down": 0}
                if random.random() < 0.7:
                    votes[strat]["up"] += 1
                else:
                    votes[strat]["down"] += 1

    with open(VOTES_PATH, "w") as f:
        json.dump(votes, f, indent=2)
    print(f"🗳 Votes cast for {len(votes)} strategies.")

if __name__ == "__main__":
    simulate_vote()

import json
import random

AGENT_PATH = "agents/agent_registry.json"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
VOTE_LOG = "agents/debate_votes.json"

def run_debate():
    with open(AGENT_PATH) as f:
        agents = json.load(f)
    with open(LINEAGE_PATH) as f:
        lineage = json.load(f)

    votes = {}
    for agent, strategies in agents.items():
        for s in lineage:
            if "auto" in s or "proposal" in s:
                if s not in votes:
                    votes[s] = 0
                score = 0

                if s in strategies:
                    score += 2  # support own strategies
                if "Hybrid" in lineage[s].get("rating", ""):
                    score += 1
                if "Poor" in lineage[s].get("rating", ""):
                    score -= 2
                if random.random() > 0.8:
                    score += 1

                votes[s] += score

    with open(VOTE_LOG, "w") as f:
        json.dump(votes, f, indent=2)

    print(f"🤖 Agent debate votes written to {VOTE_LOG}")

if __name__ == "__main__":
    run_debate()
    
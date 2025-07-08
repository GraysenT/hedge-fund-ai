import json
import os

MEMORY_PATH = "agents/agent_long_term_memory.json"
RANKS_PATH = "agents/agent_rankings.json"

def run_meta_ceo():
    memory = json.load(open(MEMORY_PATH))
    scores = {}

    for agent, info in memory.items():
        pnl = info.get("pnl", 0)
        trades = len(info["trades"])
        mutations = len(info["mutations"])
        score = pnl + 5 * mutations + 0.1 * trades
        scores[agent] = round(score, 2)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    new_ranks = {agent: {"rank": i+1, "score": score} for i, (agent, score) in enumerate(ranked)}

    with open(RANKS_PATH, "w") as f:
        json.dump(new_ranks, f, indent=2)

    print("🏆 Agent Rankings Updated:")
    for a, s in new_ranks.items():
        print(f"{a}: #{s['rank']} | Score: {s['score']}")

if __name__ == "__main__":
    run_meta_ceo()
    
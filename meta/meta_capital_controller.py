import json
import os

TOURNAMENT_PATH = "agents/agent_tournament_results.json"
OUTPUT_PATH = "agents/agent_capital_weights.json"

def score_agents():
    if not os.path.exists(TOURNAMENT_PATH):
        print("❌ Tournament results not found.")
        return {}

    with open(TOURNAMENT_PATH) as f:
        data = json.load(f)

    scores = {}
    for agent, info in data.items():
        pnl = max(0, info["pnl"])  # clamp negatives to 0
        consistency = max(0, info["pnl"] / max(1, info["days"]))
        score = pnl + (consistency * 1000)
        scores[agent] = round(score, 2)

    return scores

def assign_weights(scores):
    total = sum(scores.values())
    if total == 0:
        print("⚠️ No positive scores to allocate capital.")
        return {agent: 0.0 for agent in scores}

    weights = {agent: round(s / total, 4) for agent, s in scores.items()}
    return weights

def save_weights(weights):
    with open(OUTPUT_PATH, "w") as f:
        json.dump(weights, f, indent=2)
    print(f"\n💼 Meta-Agent Capital Allocations saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    print("📊 Calculating meta-agent capital weights...")
    scores = score_agents()
    weights = assign_weights(scores)

    for agent, w in weights.items():
        print(f"{agent}: {round(w * 100, 2)}%")

    save_weights(weights)
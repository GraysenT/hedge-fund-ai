import json
import os
import random

RESEARCH_DB = "memory/research_memory.json"
DEPLOY_DB = "memory/deployability_scores.json"

def score_strategy_deployability():
    if not os.path.exists(RESEARCH_DB):
        print("❌ No hypotheses found.")
        return

    with open(RESEARCH_DB, "r") as f:
        ideas = json.load(f)

    scores = []
    for i in ideas:
        score = {
            "strategy": i.get("strategy", i.get("id", "unknown")),
            "idea": i["idea"],
            "sim_score": i["score"],
            "robustness": round(random.uniform(0.6, 1.0), 2),
            "explainability": round(random.uniform(0.5, 1.0), 2),
            "risk_rating": round(random.uniform(0.2, 0.9), 2),
        }

        # ✅ Properly use 'deployability' key now
        score["deployability"] = round(
            0.4 * score["sim_score"]
            + 0.2 * score["robustness"]
            + 0.2 * score["explainability"]
            - 0.2 * score["risk_rating"],
            3
        )

        scores.append(score)

    with open(DEPLOY_DB, "w") as f:
        json.dump(scores, f, indent=2)

    print(f"✅ Scored {len(scores)} strategies for deployability.")

if __name__ == "__main__":
    score_strategy_deployability()
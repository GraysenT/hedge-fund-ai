import os
import json
import random

FUND_DIR = "memory/funds/"
OUTPUT_PATH = "memory/fund_weights.json"

def allocate_across_funds():
    fund_weights = {}
    fund_scores = {}

    for fund in os.listdir(FUND_DIR):
        path = os.path.join(FUND_DIR, fund, "allocations.json")
        if not os.path.exists(path):
            continue

        with open(path) as f:
            strategies = json.load(f)
        score = sum(s["weight"] for s in strategies)
        risk_penalty = random.uniform(0.8, 1.2)
        fund_scores[fund] = score / risk_penalty

    total_score = sum(fund_scores.values()) or 1
    for fund, score in fund_scores.items():
        fund_weights[fund] = round(score / total_score, 4)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(fund_weights, f, indent=2)

    print("🏦 Fund-of-Funds Allocator updated fund weights.")
    return fund_weights

if __name__ == "__main__":
    allocate_across_funds()
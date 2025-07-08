import json
import os

CONF_RISK_DB = "memory/confidence_vs_risk.json"
REWARD_DB = "memory/reinforcement_rewards.json"
ALLOC_DB = "memory/optimized_allocations.json"

def update_strategy_weights():
    if not os.path.exists(CONF_RISK_DB):
        print("❌ Confidence vs Risk data missing.")
        return

    with open(CONF_RISK_DB, "r") as f:
        cr_data = json.load(f)

    # Load reinforcement rewards if available
    if os.path.exists(REWARD_DB):
        with open(REWARD_DB, "r") as f:
            rewards = {r["id"]: r["reward"] for r in json.load(f)}
    else:
        rewards = {}

    updated = []
    for strat in cr_data:
        idea = strat["idea"]
        reward = rewards.get(idea, 0)
        signal_strength = strat["signal_strength"]
        confidence = strat["confidence"]
        risk = strat["risk"]

        weight = max(0.01, signal_strength + 0.1 * reward + 0.2 * (confidence - risk))
        updated.append({"strategy": idea, "weight": round(weight, 4)})

    total = sum(u["weight"] for u in updated) or 1
    normalized = [
        {"strategy": u["strategy"], "weight": round(u["weight"] / total, 4)}
        for u in updated
    ]

    with open(ALLOC_DB, "w") as f:
        json.dump(normalized, f, indent=2)

    print(f"💰 Allocations updated for {len(normalized)} strategies.")

if __name__ == "__main__":
    update_strategy_weights()
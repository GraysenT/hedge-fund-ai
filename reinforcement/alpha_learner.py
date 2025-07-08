import os
import json
import random

REWARD_LOG = "memory/reinforcement_rewards.json"
ALLOCATION_LOG = "memory/optimized_allocations.json"

def update_strategy_weights_by_reward():
    if not os.path.exists(REWARD_LOG) or not os.path.exists(ALLOCATION_LOG):
        return

    with open(REWARD_LOG) as f:
        rewards = {r["id"]: r["reward"] for r in json.load(f)}

    with open(ALLOCATION_LOG) as f:
        allocations = json.load(f)

    new_allocs = []
    for strat in allocations:
        reward = rewards.get(strat["strategy"], 0)
        scaled = strat["weight"] * (1 + 0.2 * reward)
        new_allocs.append({"strategy": strat["strategy"], "weight": round(scaled, 4)})

    total = sum(a["weight"] for a in new_allocs) or 1
    normalized = [{"strategy": a["strategy"], "weight": round(a["weight"] / total, 4)} for a in new_allocs]

    with open(ALLOCATION_LOG, "w") as f:
        json.dump(normalized, f, indent=2)

    print("🤖 Alpha learner updated strategy weights based on rewards.")

if __name__ == "__main__":
    update_strategy_weights_by_reward()
import json
import os

CONF_RISK_DB = "memory/confidence_vs_risk.json"
REWARD_DB = "memory/reinforcement_rewards.json"
ALLOC_DB = "memory/optimized_allocations.json"

def optimize_capital_allocation():
    if not os.path.exists(CONF_RISK_DB):
        print("❌ Missing confidence-risk data.")
        return

    with open(CONF_RISK_DB, "r") as f:
        cr_data = json.load(f)

    if os.path.exists(REWARD_DB):
        with open(REWARD_DB, "r") as f:
            rewards = {r["id"]: r["reward"] for r in json.load(f)}
    else:
        rewards = {}

    allocations = []
    for strat in cr_data:
        idea = strat["idea"]
        score = (
            0.5 * strat["signal_strength"]
            + 0.3 * strat["confidence"]
            - 0.2 * strat["risk"]
            + 0.4 * rewards.get(idea, 0)
        )
        allocations.append((idea, max(score, 0)))

    total = sum(w for _, w in allocations) or 1
    normalized = [{"strategy": i, "weight": round(w / total, 4)} for i, w in allocations]

    with open(ALLOC_DB, "w") as f:
        json.dump(normalized, f, indent=2)

    print(f"💰 Capital allocations optimized for {len(normalized)} strategies.")

if __name__ == "__main__":
    optimize_capital_allocation()
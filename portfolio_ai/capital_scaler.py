import json
import os
from datetime import datetime

def scale_capital_allocations(strategy_lineage, deployment_status):
    """
    Scale capital allocation for each approved strategy based on Sharpe, depth, and agent tournament results.
    """
    scaled = {}

    for strat, info in strategy_lineage.items():
        if strat not in deployment_status or not deployment_status[strat].get("approved"):
            continue

        sharpe = info.get("sharpe", 0)
        depth = info.get("depth", 0)

        # Base weight
        base = 1.0

        # Scale by Sharpe (clip to [0, 2])
        sharpe_weight = max(0.0, min(2.0, sharpe + 1))

        # Penalize shallow strategies
        depth_penalty = 1.0 if depth >= 2 else 0.5

        # Final base weight
        final = round(base * sharpe_weight * depth_penalty, 3)
        scaled[strat] = final

    # 🔺 Promote top agent strategies
    AGENT_TOURNAMENT = "agents/agent_tournament_results.json"
    if os.path.exists(AGENT_TOURNAMENT):
        with open(AGENT_TOURNAMENT) as f:
            agent_results = json.load(f)
        top_agents = sorted(agent_results.items(), key=lambda x: x[1]["pnl"], reverse=True)[:1]
        top_strats = top_agents[0][1]["strategies"] if top_agents else []
        for strat in scaled:
            if strat in top_strats:
                print(f"💹 Promoting {strat} (top agent member) → +25% capital boost.")
                scaled[strat] = round(scaled[strat] * 1.25, 3)

    return scaled

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_scaled_allocations(scaled_allocs):
    date_str = datetime.now().strftime("%Y-%m-%d")
    folder = "memory/scaled_allocations"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{date_str}.json")

    with open(path, "w") as f:
        json.dump(scaled_allocs, f, indent=2)
    print(f"✅ Saved scaled capital allocations to {path}")

if __name__ == "__main__":
    lineage = load_json("strategy_memory/strategy_lineage.json")
    deployment = load_json("strategy_memory/deployment_status.json")  # should exist from router

    scaled = scale_capital_allocations(lineage, deployment)
    for strat, weight in scaled.items():
        print(f"📊 {strat}: capital weight = {weight}")
    save_scaled_allocations(scaled)
    
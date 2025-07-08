import os
import json
import pandas as pd
from collections import defaultdict

SNAPSHOT_DIR = "strategy_memory/history"

# Parameters
SURVIVAL_MIN_SHARPE = 1.0
DECAY_THRESHOLD = 0.3


def load_snapshots():
    files = sorted([f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json")], reverse=True)
    all_snapshots = []
    for file in files:
        with open(os.path.join(SNAPSHOT_DIR, file), 'r') as f:
            snap = json.load(f)
            snap_ts = snap.get("timestamp")
            weights = snap.get("final_weights", {})
            performance = snap.get("strategy_performance", {})
            all_snapshots.append((snap_ts, weights, performance))
    return all_snapshots


def score_survival(snapshots):
    strategy_scores = defaultdict(lambda: {"count": 0, "avg_weight": 0, "avg_sharpe": 0})

    for _, weights, performance in snapshots:
        for strat, weight in weights.items():
            if not strat.startswith("gen_strat"):
                continue
            strategy_scores[strat]["count"] += 1
            strategy_scores[strat]["avg_weight"] += weight
            if isinstance(performance, dict) and strat in performance:
                strat_perf = performance.get(strat, {})
                sharpe = strat_perf.get("sharpe", 0)
                strategy_scores[strat]["avg_sharpe"] += sharpe

    results = []
    for strat, data in strategy_scores.items():
        count = data["count"]
        avg_weight = data["avg_weight"] / count
        avg_sharpe = data["avg_sharpe"] / count if data["avg_sharpe"] > 0 else 0

        if avg_sharpe >= SURVIVAL_MIN_SHARPE:
            status = "🔼 Promising"
        elif avg_sharpe < DECAY_THRESHOLD:
            status = "🔽 Decaying"
        else:
            status = "➖ Neutral"

        results.append({
            "Strategy": strat,
            "Snapshots": count,
            "Avg Weight": round(avg_weight, 4),
            "Avg Sharpe": round(avg_sharpe, 4),
            "Status": status
        })

    return pd.DataFrame(results)


if __name__ == '__main__':
    snaps = load_snapshots()
    df = score_survival(snaps)
    print("\n🧠 Generated Strategy Survival Scores:")
    if "Avg Sharpe" in df.columns:
        print(df.sort_values(by="Avg Sharpe", ascending=False).to_string(index=False))
    else:
        print(df.to_string(index=False))

import json
import os
from collections import defaultdict

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"


def compute_bias_by_depth():
    if not os.path.exists(LINEAGE_PATH):
        raise FileNotFoundError("strategy_lineage.json not found.")

    with open(LINEAGE_PATH, "r") as f:
        lineage = json.load(f)

    depth_sharpe = defaultdict(float)
    depth_counts = defaultdict(int)

    for meta in lineage.values():
        depth = meta.get("depth")
        sharpe = meta.get("sharpe", 0)
        if isinstance(depth, int):
            depth_sharpe[depth] += sharpe
            depth_counts[depth] += 1

    bias_map = {}
    for depth in depth_sharpe:
        avg_sharpe = depth_sharpe[depth] / depth_counts[depth]
        bias_map[depth] = round(avg_sharpe, 4)

    print("📊 Meta-Mutation Depth Bias Map (Avg Sharpe by Depth):")
    for d in sorted(bias_map):
        print(f"  Depth {d}: Avg Sharpe = {bias_map[d]}")

    return bias_map


if __name__ == "__main__":
    compute_bias_by_depth()

import json
import os
from collections import defaultdict

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def map_generations():
    lineage = json.load(open(LINEAGE_PATH))
    family_tree = defaultdict(list)

    for strat, info in lineage.items():
        parent = info.get("parent", "ROOT")
        family_tree[parent].append(strat)

    depth_count = {}
    for parent, children in family_tree.items():
        depth = max([lineage.get(c, {}).get("depth", 0) for c in children])
        depth_count[parent] = {"descendants": len(children), "max_depth": depth}

    print("🌳 Generational Intelligence Map:")
    for root, stats in depth_count.items():
        print(f"{root} → {stats['descendants']} children | max depth {stats['max_depth']}")

if __name__ == "__main__":
    map_generations()
    
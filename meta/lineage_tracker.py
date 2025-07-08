import os
import json
from meta.oversight_engine import load_evolution_logs, analyze_strategy_health

GEN_PATH = "strategy_memory/generated_strategies.json"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"


def build_lineage_map():
    if not os.path.exists(GEN_PATH):
        print("❌ No generated strategies found.")
        return

    with open(GEN_PATH, 'r') as f:
        strategies = json.load(f)

    # Identify recursively generated strategies
    lineage = {}
    for child in strategies:
        if child.startswith("gen_strat_r"):
            parents = [k for k in strategies if child in strategies.get(k, {})]
            if parents:
                lineage[child] = parents[0]

    with open(LINEAGE_PATH, 'w') as f:
        json.dump(lineage, f, indent=2)

    print(f"✅ Strategy lineage saved to {LINEAGE_PATH}")
    print("📚 Lineage map:")
    for child, parent in lineage.items():
        print(f" - {child} ← {parent}")

if __name__ == '__main__':
    build_lineage_map()

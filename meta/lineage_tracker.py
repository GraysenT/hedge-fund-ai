import os
import json
from meta.oversight_engine import load_evolution_logs, analyze_strategy_health

LINEAGE_FILE = "logs/lineage_map.json"
os.makedirs("logs", exist_ok=True)

def log_fork(parent_id, child_id, timestamp):
    lineage = {}
    if os.path.exists(LINEAGE_FILE):
        with open(LINEAGE_FILE) as f:
            lineage = json.load(f)
    lineage[child_id] = {"parent": parent_id, "timestamp": timestamp}
    with open(LINEAGE_FILE, "w") as f:
        json.dump(lineage, f, indent=2)

def get_lineage():
    with open(LINEAGE_FILE) as f:
        return json.load(f)

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

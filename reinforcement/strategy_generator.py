import os
import json
import random
from datetime import datetime

SNAPSHOT_DIR = "strategy_memory/history"
OUTPUT_PATH = "strategy_memory/generated_strategies.json"

# Parameters
TOP_K = 5  # Use top K strategies per snapshot
MUTATION_RATE = 0.15  # Percent change on mutation
NUM_GENERATED = 10  # How many new strategies to generate


def load_snapshots():
    files = sorted([f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json")], reverse=True)
    data = []
    for f_name in files:
        with open(os.path.join(SNAPSHOT_DIR, f_name), 'r') as f:
            snap = json.load(f)
            snap_ts = snap.get("timestamp")
            weights = snap.get("final_weights", {})
            data.append((snap_ts, weights))
    return data


def select_top_strategies(snapshots):
    top_strategies = set()
    for _, weights in snapshots:
        ranked = sorted(weights.items(), key=lambda x: abs(x[1]), reverse=True)
        top_k = [k for k, _ in ranked[:TOP_K]]
        top_strategies.update(top_k)
    return list(top_strategies)


def mutate_strategy_weights(strategies):
    generated = {}
    for i in range(NUM_GENERATED):
        strat = f"gen_strat_{i+1}"
        weights = {s: round(random.uniform(0.1, 0.5), 4) for s in strategies}
        # Apply mutation
        for s in weights:
            if random.random() < MUTATION_RATE:
                weights[s] = round(weights[s] * random.uniform(0.8, 1.2), 4)
        generated[strat] = weights
    return generated


def save_generated(generated):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(generated, f, indent=2)
    print(f"✅ Generated strategies saved to {OUTPUT_PATH}")


if __name__ == '__main__':
    snapshots = load_snapshots()
    top_strats = select_top_strategies(snapshots)
    generated = mutate_strategy_weights(top_strats)
    save_generated(generated)

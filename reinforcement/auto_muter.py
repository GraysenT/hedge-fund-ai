import os
import json
from reinforcement.survival_tracker import load_snapshots, score_survival

BASE_PATH = "strategy_memory/base_weights.json"
REINFORCE_PATH = "strategy_memory/latest_weights.json"
MUTED_TAG = "muted"

def load_weights(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_weights(path, weights):
    with open(path, 'w') as f:
        json.dump(weights, f, indent=2)

def mute_decaying_strategies():
    snapshots = load_snapshots()
    df = score_survival(snapshots)
    decaying_strats = df[df["Status"] == "🔽 Decaying"]["Strategy"].tolist()

    if not decaying_strats:
        print("✅ No decaying strategies to mute.")
        return

    base = load_weights(BASE_PATH)
    reinforce = load_weights(REINFORCE_PATH)

    for strat in decaying_strats:
        if strat in base:
            base[strat] = 0.0
        if strat in reinforce:
            reinforce[strat] = 0.0

    save_weights(BASE_PATH, base)
    save_weights(REINFORCE_PATH, reinforce)

    print(f"🔇 Muted {len(decaying_strats)} decaying strategies:")
    for s in decaying_strats:
        print(f" - {s}")

if __name__ == '__main__':
    mute_decaying_strategies()
    
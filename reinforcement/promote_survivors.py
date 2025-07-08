import os
import json
from reinforcement.survival_tracker import load_snapshots, score_survival

BASE_PATH = "strategy_memory/base_weights.json"
REINFORCE_PATH = "strategy_memory/latest_weights.json"
PROMOTE_BONUS = 1.25


def load_weights(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_weights(path, weights):
    with open(path, 'w') as f:
        json.dump(weights, f, indent=2)

def promote_promising_strategies():
    snapshots = load_snapshots()
    df = score_survival(snapshots)
    promising_strats = df[df["Status"] == "🔼 Promising"]["Strategy"].tolist()

    if not promising_strats:
        print("✅ No promising strategies found to promote.")
        return

    base = load_weights(BASE_PATH)
    reinforce = load_weights(REINFORCE_PATH)

    for strat in promising_strats:
        if strat in base:
            base[strat] = round(base[strat] * PROMOTE_BONUS, 4)
        if strat in reinforce:
            reinforce[strat] = round(reinforce[strat] * PROMOTE_BONUS, 4)

    save_weights(BASE_PATH, base)
    save_weights(REINFORCE_PATH, reinforce)

    print(f"🚀 Promoted {len(promising_strats)} strong survivors:")
    for s in promising_strats:
        print(f" - {s}")

if __name__ == '__main__':
    promote_promising_strategies()
    
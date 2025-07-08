import json
import os
from dashboards.alpha_monitor import pivot

def load_alpha_health():
    rolling = pivot.rolling(window=5).mean().dropna()
    return rolling.mean().to_dict()

def reinforce_weights(base_weights):
    alpha_scores = load_alpha_health()
    reinforced = {}

    for strat, base in base_weights.items():
        alpha = alpha_scores.get(strat, 0)
        multiplier = 1.2 if alpha > 0 else 0.8
        reinforced[strat] = round(base * multiplier, 3)

        if multiplier > 1:
            print(f"🟢 {strat} rewarded (↑ alpha) → +20%")
        else:
            print(f"🔻 {strat} penalized (↓ alpha) → -20%")

    return reinforced

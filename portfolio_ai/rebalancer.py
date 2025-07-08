import json
import os

BASE_WEIGHTS_PATH = "strategy_memory/base_weights.json"
REINFORCED_WEIGHTS_PATH = "strategy_memory/latest_weights.json"
POSITION_TAGS_PATH = "strategy_memory/long_short_tags.json"
REBALANCED_OUTPUT_PATH = "strategy_memory/rebalanced_weights.json"

NET_EXPOSURE_LIMIT = 1.0
GROSS_EXPOSURE_LIMIT = 1.5


def load_weights(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def apply_long_short_logic(weights, tags):
    rebalanced = {}
    for strat, weight in weights.items():
        tag = tags.get(strat, "long")
        signed_weight = weight if tag == "long" else -weight
        rebalanced[strat] = signed_weight
    return rebalanced


def enforce_exposure_limits(signed_weights):
    gross = sum(abs(w) for w in signed_weights.values())
    net = sum(signed_weights.values())

    scale = 1.0
    if gross > GROSS_EXPOSURE_LIMIT:
        scale = min(scale, GROSS_EXPOSURE_LIMIT / gross)
    if abs(net) > NET_EXPOSURE_LIMIT:
        scale = min(scale, NET_EXPOSURE_LIMIT / abs(net))

    for strat in signed_weights:
        signed_weights[strat] = round(signed_weights[strat] * scale, 4)

    return signed_weights, scale


def run_rebalancer():
    base = load_weights(BASE_WEIGHTS_PATH)
    reinforced = load_weights(REINFORCED_WEIGHTS_PATH)
    tags = load_weights(POSITION_TAGS_PATH)

    # Apply reinforcement to base weights
    adjusted = {k: base.get(k, 0) * reinforced.get(k, 1.0) for k in base}
    signed = apply_long_short_logic(adjusted, tags)
    final, scale = enforce_exposure_limits(signed)

    print("\n✅ Rebalanced Strategy Weights (Net/Gross limits applied):")
    for k, v in final.items():
        print(f"{k}: {v}")
    print(f"\n📉 Exposure Scaling Applied: {scale:.4f}")

    os.makedirs("strategy_memory", exist_ok=True)
    with open(REBALANCED_OUTPUT_PATH, 'w') as f:
        json.dump(final, f, indent=2)
    print(f"📁 Saved to {REBALANCED_OUTPUT_PATH}")

    return final


if __name__ == "__main__":
    run_rebalancer()

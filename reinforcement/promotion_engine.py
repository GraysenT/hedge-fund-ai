import os
import json

GEN_PATH = "strategy_memory/generated_strategies.json"
BASE_PATH = "strategy_memory/base_weights.json"
TAGS_PATH = "strategy_memory/long_short_tags.json"

DEFAULT_WEIGHT = 0.25
DEFAULT_TAG = "long"


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def promote_strategies(selected_strats):
    gen = load_json(GEN_PATH)
    base = load_json(BASE_PATH)
    tags = load_json(TAGS_PATH)

    for strat in selected_strats:
        if strat not in gen:
            print(f"⚠️ Skipping unknown strategy: {strat}")
            continue
        for original, weight in gen[strat].items():
            promoted_name = f"{strat}_{original}"
            base[promoted_name] = round(weight, 4)
            tags[promoted_name] = DEFAULT_TAG

    os.makedirs("strategy_memory", exist_ok=True)
    with open(BASE_PATH, 'w') as f:
        json.dump(base, f, indent=2)
    with open(TAGS_PATH, 'w') as f:
        json.dump(tags, f, indent=2)

    print(f"✅ Promoted {len(selected_strats)} strategies into live base weights.")


if __name__ == '__main__':
    # Example: promote_strategies(['gen_strat_1', 'gen_strat_3'])
    promote_strategies(["gen_strat_1", "gen_strat_2"])

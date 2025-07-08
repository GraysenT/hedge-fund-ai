import os
import json
import random
from itertools import combinations

GEN_PATH = "strategy_memory/generated_strategies.json"
CLAN_TAG_PATH = "strategy_memory/strategy_clans.json"
OUTPUT_PATH = "strategy_memory/generated_strategies.json"

NUM_CROSS_CHILDREN = 3


def load_json(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing: {path}")
    with open(path, 'r') as f:
        return json.load(f)


def recombine_weights(w1, w2):
    keys = set(w1.keys()).union(w2.keys())
    child = {}
    for k in keys:
        v1 = w1.get(k, 0)
        v2 = w2.get(k, 0)
        avg = (v1 + v2) / 2
        child[k] = round(avg * random.uniform(0.9, 1.1), 4)
    return child


def recombination_engine():
    gen = load_json(GEN_PATH)
    clans = load_json(CLAN_TAG_PATH)

    # Invert clans
    clan_map = {}
    for strat, clan in clans.items():
        clan_map.setdefault(clan, []).append(strat)

    cross_pairs = list(combinations(clan_map.keys(), 2))
    cross_children = {}
    counter = 1

    for clan_a, clan_b in cross_pairs:
        parent_a = random.choice(clan_map[clan_a])
        parent_b = random.choice(clan_map[clan_b])

        w1 = gen.get(parent_a, {})
        w2 = gen.get(parent_b, {})

        for i in range(NUM_CROSS_CHILDREN):
            child_name = f"gen_strat_xcross_{counter}"
            child_weights = recombine_weights(w1, w2)
            cross_children[child_name] = child_weights
            counter += 1

    gen.update(cross_children)

    with open(OUTPUT_PATH, 'w') as f:
        json.dump(gen, f, indent=2)

    print(f"✅ Created {len(cross_children)} crossover strategies from {len(cross_pairs)} clan pairs.")
    for strat in cross_children:
        print(f" - {strat}")


if __name__ == '__main__':
    recombination_engine()
import json
import os
import random
from utils.paths import STRATEGY_STATUS_FILE, MODULE_QUEUE_FILE

def creative_suffix():
    return random.choice([
        "prime", "edge", "fusion", "echo", "reborn", "vision", "plus", "vortex"
    ])

def mutate_strategy_name(base_name):
    suffix = creative_suffix()
    base = base_name.split("/")[-1].replace(".py", "")
    return f"{base}_{suffix}"

def generate_mutated_strategies(top_n=3):
    if not os.path.exists(STRATEGY_STATUS_FILE):
        return []

    with open(STRATEGY_STATUS_FILE, "r") as f:
        scores = json.load(f)

    sorted_strats = sorted(scores.items(), key=lambda x: x[1].get("sharpe", 0), reverse=True)
    top_strats = [name for name, _ in sorted_strats[:top_n]]

    ideas = []
    for strat in top_strats:
        mutated = mutate_strategy_name(strat)
        path = f"strategies/{mutated}.py"
        desc = f"A self-evolved variant of {strat} with enhanced logic."
        ideas.append((path, desc))

    return ideas

def append_mutations_to_queue():
    if not os.path.exists(MODULE_QUEUE_FILE):
        queue = {}
    else:
        with open(MODULE_QUEUE_FILE, "r") as f:
            queue = json.load(f)

    ideas = generate_mutated_strategies()
    added = 0

    for path, desc in ideas:
        if path not in queue:
            queue[path] = desc
            added += 1

    with open(MODULE_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

    print(f"[MUTATION] Added {added} mutated strategies to queue.")

if __name__ == "__main__":
    append_mutations_to_queue()
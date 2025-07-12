import os
import json
import random
from utils.paths import MODULE_QUEUE_FILE

# Track what’s already been built
def get_existing_modules(base_dir="strategies"):
    existing = []
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".py"):
                relative_path = os.path.join(root, f).replace("\\", "/")
                if relative_path.startswith("./"):
                    relative_path = relative_path[2:]
                existing.append(relative_path)
    return set(existing)

# Generate new idea variants
def generate_new_ideas(n=5):
    prefixes = ["dark_pool", "macro", "overnight", "fed_day", "crypto", "volatility", "volume", "momentum", "mean_reversion"]
    suffixes = ["scalper", "hedger", "tracker", "arbitrage", "booster", "signalizer", "sniper", "rotator", "predictor"]
    new_ideas = []

    for _ in range(n * 2):  # Generate more than needed, filter later
        name = f"strategies/{random.choice(prefixes)}_{random.choice(suffixes)}.py"
        desc = f"A strategy that blends {random.choice(prefixes)} signals with {random.choice(suffixes)} behavior."
        new_ideas.append((name, desc))

    return new_ideas

# Append only new items to queue
def append_to_queue():
    if not os.path.exists(MODULE_QUEUE_FILE):
        queue = {}
    else:
        with open(MODULE_QUEUE_FILE, "r") as f:
            queue = json.load(f)

    built = get_existing_modules("strategies")
    queue_paths = set(queue.keys())

    new_ideas = generate_new_ideas()
    added = 0

    for path, desc in new_ideas:
        if path not in queue_paths and path not in built:
            queue[path] = desc
            added += 1
        if added >= 5:
            break

    with open(MODULE_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

    print(f"[IDEATOR] Added {added} new strategy modules to queue.")

if __name__ == "__main__":
    append_to_queue()
import os
import json
import random
import uuid

STRAT_PATH = "strategies/"
GEN_PATH = "strategies/generated/"
os.makedirs(GEN_PATH, exist_ok=True)

def load_strategy_code(name):
    try:
        with open(os.path.join(STRAT_PATH, name), "r") as f:
            return f.readlines()
    except:
        return []

def crossover_strategies(parent_a, parent_b):
    lines_a = load_strategy_code(parent_a)
    lines_b = load_strategy_code(parent_b)

    if not lines_a or not lines_b:
        print("❌ Failed to load parents.")
        return

    # Cut halfway and splice
    split_a = len(lines_a) // 2
    split_b = len(lines_b) // 2
    child_code = lines_a[:split_a] + lines_b[split_b:]

    child_name = f"cross_{uuid.uuid4().hex[:6]}.py"
    with open(os.path.join(GEN_PATH, child_name), "w") as f:
        f.writelines(["# Offspring of: ", parent_a, " + ", parent_b, "\n\n"] + child_code)

    print(f"🧬 Created crossover strategy: {child_name}")
    return child_name

if __name__ == "__main__":
    all_strats = [f for f in os.listdir(STRAT_PATH) if f.endswith(".py")]
    if len(all_strats) >= 2:
        crossover_strategies(random.choice(all_strats), random.choice(all_strats))
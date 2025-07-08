import random
import uuid
import os

STRATEGY_DIR = "strategies/"
GEN_DIR = "strategies/generated/"
os.makedirs(GEN_DIR, exist_ok=True)

def clone_mutate_strategy(filename):
    with open(os.path.join(STRATEGY_DIR, filename), "r") as f:
        lines = f.readlines()

    mutated = []
    for line in lines:
        if "threshold" in line or ">" in line or "<" in line:
            line = line.replace("0.5", str(round(random.uniform(0.3, 0.7), 2)))
        mutated.append(line)

    new_name = f"gen_strat_{uuid.uuid4().hex[:6]}.py"
    with open(os.path.join(GEN_DIR, new_name), "w") as f:
        f.writelines(mutated)

    print(f"🧬 Generated {new_name} from {filename}")

if __name__ == "__main__":
    base_strats = [f for f in os.listdir(STRATEGY_DIR) if f.endswith(".py")]
    for f in base_strats[:2]:
        clone_mutate_strategy(f)
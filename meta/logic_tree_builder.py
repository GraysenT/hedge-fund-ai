import json
import os

STRATEGY_PATH = "strategies/"

def extract_logic_tree(strategy_file):
    logic_tree = []
    with open(os.path.join(STRATEGY_PATH, strategy_file), "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if "if " in line or "elif " in line or "return" in line:
            logic_tree.append(line)

    return {
        "strategy": strategy_file,
        "logic_tree": logic_tree
    }

if __name__ == "__main__":
    files = [f for f in os.listdir(STRATEGY_PATH) if f.endswith(".py")]
    for f in files:
        tree = extract_logic_tree(f)
        print(f"\n📘 Logic Tree from {f}")
        for line in tree["logic_tree"]:
            print("  ", line)
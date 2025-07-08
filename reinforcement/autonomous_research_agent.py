from meta.hypothesis_engine import generate_hypothesis
from meta.logic_tree_builder import extract_logic_tree
import os
import random

def run_research_loop():
    strategy_files = [f for f in os.listdir("strategies") if f.endswith(".py")]
    chosen = random.choice(strategy_files)
    logic = extract_logic_tree(chosen)

    idea = f"Explore variation of: {logic['logic_tree'][0][:100]}..."
    context = "\n".join(logic["logic_tree"])
    simulation_score = round(random.uniform(0.4, 1.0), 3)

    generate_hypothesis(idea, context, simulation_score)

if __name__ == "__main__":
    for _ in range(3):
        run_research_loop()
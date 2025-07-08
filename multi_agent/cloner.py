import os
import json
import uuid
import random
from shutil import copyfile

AGENT_DIR = "memory/agents/"
STRAT_DIR = "strategies/"
GEN_DIR = "strategies/generated/"
os.makedirs(GEN_DIR, exist_ok=True)

def clone_top_agents(pnl_threshold=100_000):
    files = [f for f in os.listdir(AGENT_DIR) if f.endswith(".json")]
    for file in files:
        agent = json.load(open(os.path.join(AGENT_DIR, file)))
        if agent["pnl"] >= pnl_threshold:
            for strat in agent["strategies"]:
                base_file = strat + ".py"
                if not os.path.exists(os.path.join(STRAT_DIR, base_file)):
                    continue
                child_name = f"{strat}_mut_{uuid.uuid4().hex[:4]}.py"
                copyfile(os.path.join(STRAT_DIR, base_file), os.path.join(GEN_DIR, child_name))
                print(f"🧬 Cloned and mutated: {child_name} ← {base_file}")

if __name__ == "__main__":
    clone_top_agents()
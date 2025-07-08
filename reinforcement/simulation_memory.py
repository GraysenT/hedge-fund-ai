import json
import os
from datetime import datetime
import random

SIM_MEM_PATH = "memory/simulation_memory.json"
os.makedirs("memory", exist_ok=True)

def update_simulation_memory():
    # Simulated memory of past strategy performance
    fake_memory = []

    for strategy in ["stat_arb", "momentum", "macro_sentiment", "crypto_edge"]:
        entry = {
            "strategy": strategy,
            "reward": round(random.uniform(-0.5, 1.5), 3),
            "timestamp": datetime.utcnow().isoformat()
        }
        fake_memory.append(entry)

    with open(SIM_MEM_PATH, "w") as f:
        json.dump(fake_memory, f, indent=2)

    print(f"🧠 Simulation memory updated for {len(fake_memory)} strategies.")

if __name__ == "__main__":
    update_simulation_memory()
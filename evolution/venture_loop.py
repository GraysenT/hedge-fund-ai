from worldbuilder.economy_sim import EconomySim
from oracle.meta_oracle import ask_oracle
import time
import json
import os

sim = EconomySim(seeds=10)

log_file = "logs/ventures.jsonl"
os.makedirs("logs", exist_ok=True)

while True:
    sim.step()
    top = sim.top(1)[0]

    if top.capital > 2000:
        suggestion = ask_oracle(top.vision, "How can this venture be improved?")
        print(f"🧠 Oracle on {top.vision}:\n{suggestion}")

        log = {
            "vision": top.vision,
            "capital": top.capital,
            "oracle": suggestion,
            "timestamp": time.time()
        }

        with open(log_file, "a") as f:
            f.write(json.dumps(log) + "\n")

    time.sleep(2)
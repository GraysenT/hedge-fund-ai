import json
import time
from economy.business_seed import BusinessSeed

# Simulated peer
with open("mesh/incoming_ventures.jsonl") as f:
    for line in f:
        idea = json.loads(line)["vision"]
        seed = BusinessSeed(idea)
        print(f"🛰 Imported venture: {idea}")
        seed.simulate_tick(25)
        print(f"🌱 New capital: {seed.capital}")
        time.sleep(1)
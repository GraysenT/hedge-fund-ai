from economy.business_seed import BusinessSeed
import random
import json
import os
from datetime import datetime

class EconomySim:
    def __init__(self, seeds=10):
        self.seeds = [BusinessSeed(f"venture_{i}") for i in range(seeds)]
        self.tick_count = 0
        self.log_path = "logs/venture_ticks.jsonl"
        os.makedirs("logs", exist_ok=True)

    def step(self):
        market_pulse = random.uniform(-20, 40)
        self.tick_count += 1
        tick_log = {
            "tick": self.tick_count,
            "market_pulse": market_pulse,
            "timestamp": datetime.utcnow().isoformat(),
            "ventures": []
        }

        for seed in self.seeds:
            gain = seed.simulate_tick(market_pulse)
            tick_log["ventures"].append({
                "id": seed.id,
                "vision": seed.vision,
                "capital": round(seed.capital, 2),
                "success": round(seed.success, 2),
                "gain": round(gain, 2)
            })

        with open(self.log_path, "a") as f:
            f.write(json.dumps(tick_log) + "\n")

    def top(self, k=5):
        return sorted(self.seeds, key=lambda s: s.capital, reverse=True)[:k]

    def add_venture(self, vision: str):
        new_seed = BusinessSeed(vision)
        self.seeds.append(new_seed)
        return new_seed
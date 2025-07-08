import time
import random
import json
import os
from datetime import datetime

TICK_LOG = "logs/tick_events.json"

def simulate_ticks(asset="AAPL"):
    os.makedirs("logs", exist_ok=True)
    ticks = []

    for _ in range(10):
        tick = {
            "timestamp": datetime.utcnow().isoformat(),
            "asset": asset,
            "price": round(random.uniform(100, 200), 2),
            "volume": random.randint(100, 1000)
        }
        ticks.append(tick)
        time.sleep(0.1)

    with open(TICK_LOG, "w") as f:
        json.dump(ticks, f, indent=2)

    print(f"⚡ Simulated {len(ticks)} ticks for {asset}.")
    return ticks

if __name__ == "__main__":
    simulate_ticks()
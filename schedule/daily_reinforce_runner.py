import time
from datetime import datetime
from portfolio_ai.reinforcement_engine import reinforce_weights
import json
import os

def load_weights():
    path = "memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]
    with open(path) as f:
        return json.load(f)

def save_reinforced(weights):
    folder = "memory/reinforced_weights"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(f"{folder}/{date_str}.json", "w") as f:
        json.dump(weights, f, indent=2)
    print(f"✅ Reinforced weights saved to {folder}/{date_str}.json")

if __name__ == "__main__":
    while True:
        now = datetime.now()
        if now.hour == 21 and now.minute == 30:
            base = load_weights()
            reinforced = reinforce_weights(base)
            save_reinforced(reinforced)
            time.sleep(60)
        else:
            time.sleep(30)

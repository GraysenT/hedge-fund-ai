import json
import random
import os
from datetime import datetime

GRAVEYARD = "strategy_memory/graveyard.json"
LINEAGE = "strategy_memory/strategy_lineage.json"

def revive():
    graveyard = json.load(open(GRAVEYARD))
    lineage = json.load(open(LINEAGE))

    candidates = [k for k, v in graveyard.items() if abs(v["pnl"]) < 100]
    if not candidates:
        print("❌ No suitable strategies to revive.")
        return

    to_rebirth = random.choice(candidates)
    new_name = f"{to_rebirth}_reborn_{random.randint(1000,9999)}"
    model = random.choice(["LSTM", "Transformer"])

    lineage[new_name] = {
        "parent": to_rebirth,
        "depth": 1,
        "model": model,
        "rating": "🧬 Reborn",
        "created": datetime.now().isoformat()
    }

    json.dump(lineage, open(LINEAGE, "w"), indent=2)
    print(f"🔁 Strategy {to_rebirth} reborn as {new_name} using model {model}")

if __name__ == "__main__":
    revive()
    
import json
import os
from datetime import datetime

GRAVEYARD = "strategy_memory/graveyard.json"
PERF_PATH = "memory/performance"

def bury_strategies(threshold=-50):
    file = sorted(os.listdir(PERF_PATH))[-1]
    perf = json.load(open(f"{PERF_PATH}/{file}"))

    graveyard = json.load(open(GRAVEYARD)) if os.path.exists(GRAVEYARD) else {}

    for strat, res in perf.items():
        if res["pnl"] < threshold:
            graveyard[strat] = {
                "pnl": res["pnl"],
                "return": res["return_pct"],
                "burial_date": datetime.now().isoformat(),
                "reason": "Alpha decay"
            }

    with open(GRAVEYARD, "w") as f:
        json.dump(graveyard, f, indent=2)
    print(f"⚰️ Buried {len(graveyard)} strategies.")

if __name__ == "__main__":
    bury_strategies()
    
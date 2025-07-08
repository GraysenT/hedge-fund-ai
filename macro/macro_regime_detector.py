import random
from datetime import datetime
import json
import os

MACRO_LOG = "memory/macro_regime.json"

REGIMES = [
    "Reflation", "Stagflation", "Disinflation", "Growth Boom", "Recession Risk"
]

def detect_macro_regime():
    regime = random.choice(REGIMES)
    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "macro_regime": regime,
        "growth": round(random.uniform(-2, 4), 2),
        "inflation": round(random.uniform(0.5, 5.0), 2),
        "policy_rate": round(random.uniform(0, 6), 2)
    }

    with open(MACRO_LOG, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"🌐 Macro regime detected: {regime}")
    return snapshot

if __name__ == "__main__":
    detect_macro_regime()
    
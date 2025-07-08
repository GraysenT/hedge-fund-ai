import json
import os
from collections import defaultdict

META_PATH = "meta/meta_strategy_map.json"
REGIME_FILE = "meta/market_regimes.json"
PERF_PATH = "memory/performance"

def map_strategies_to_regimes():
    regimes = json.load(open(REGIME_FILE))
    score = defaultdict(lambda: defaultdict(float))

    for f in sorted(os.listdir(PERF_PATH)):
        if f not in regimes:
            continue
        regime = str(regimes[f])
        day = json.load(open(f"{PERF_PATH}/{f}"))
        for strat, info in day.items():
            score[strat][regime] += info["pnl"]

    with open(META_PATH, "w") as f:
        json.dump(score, f, indent=2)
    print(f"✅ Saved strategy-regime map to {META_PATH}")

if __name__ == "__main__":
    map_strategies_to_regimes()
    
import json
import os
from collections import defaultdict

REGIME_FILE = "meta/market_regimes.json"
PERF_PATH = "memory/performance"

def build_meta_map():
    regimes = json.load(open(REGIME_FILE))
    meta_map = defaultdict(lambda: defaultdict(float))

    for f in sorted(os.listdir(PERF_PATH)):
        if f not in regimes:
            continue
        regime = str(regimes[f])
        daily = json.load(open(f"{PERF_PATH}/{f}"))
        for strat, info in daily.items():
            meta_map[strat][regime] += info["pnl"]

    print("🧠 Meta-Learning Map (strategy → regime → PnL):")
    for strat, scores in meta_map.items():
        print(f"{strat}: {dict(scores)}")

def load_logs():
    logs = []
    for folder in ["logs/dream_logs", "logs/fork_logs", "logs/trades"]:
        for file in os.listdir(folder):
            if file.endswith(".json"):
                with open(os.path.join(folder, file)) as f:
                    logs.append(json.load(f))
    return logs

def analyze_performance():
    logs = load_logs()
    insights = []
    for entry in logs:
        if isinstance(entry, dict) and "sharpe" in entry and entry["sharpe"] > 1.5:
            insights.append(entry)
    return insights

if __name__ == "__main__":
    build_meta_map()
    
import random
import json
from datetime import datetime

CONFIG_LOG = "models/auto_tuned_config.json"

def random_config():
    return {
        "model": random.choice(["LSTM", "Transformer"]),
        "layers": random.randint(1, 3),
        "lookback": random.choice([20, 30, 60]),
        "dropout": round(random.uniform(0.1, 0.4), 2),
        "confidence_threshold": round(random.uniform(0.5, 0.9), 2)
    }

def simulate_performance(config):
    base = 0.75
    boost = random.uniform(-0.05, 0.1)
    return round(base + boost, 4)

def tune():
    best = None
    best_score = 0
    for _ in range(10):
        cfg = random_config()
        score = simulate_performance(cfg)
        if score > best_score:
            best, best_score = cfg, score
    best["score"] = best_score
    best["timestamp"] = datetime.now().isoformat()

    with open(CONFIG_LOG, "w") as f:
        json.dump(best, f, indent=2)

    print(f"🛠️ Tuned config saved: {best}")

if __name__ == "__main__":
    tune()
    
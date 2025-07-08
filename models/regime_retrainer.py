import os
import json
from datetime import datetime
import random

REGIME_PATH = "meta/market_regimes.json"

def train_mock_model(symbol, regime):
    weights = {"accuracy": round(random.uniform(0.6, 0.9), 3)}
    path = f"models/{symbol}_regime_{regime}.pkl"
    with open(path, "w") as f:
        f.write(str(weights))
    print(f"✅ Trained regime model: {path}")

def run():
    os.makedirs("models", exist_ok=True)

    with open(REGIME_PATH) as f:
        regimes = json.load(f)

    for date, label in regimes.items():
        for symbol in ["AAPL", "TSLA"]:
            train_mock_model(symbol, label)

if __name__ == "__main__":
    run()

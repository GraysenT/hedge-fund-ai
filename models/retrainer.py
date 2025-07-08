import os
from datetime import datetime
import json

def retrain_lstm(symbol):
    print(f"🔁 Retraining LSTM for {symbol}...")

    model_path = f"models/{symbol}_model.pkl"
    open(model_path, "w").write("updated weights")

    metadata_path = "models/model_versions.json"
    metadata = {}

    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)

    metadata[symbol] = {
        "last_trained": datetime.now().isoformat(),
        "model_path": model_path
    }

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ Saved {symbol} model + metadata.")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    retrain_lstm("AAPL")
    retrain_lstm("TSLA")
    
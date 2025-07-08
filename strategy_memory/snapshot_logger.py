import os
import json
from datetime import datetime
from backup.s3_uploader import upload_to_s3

SNAPSHOT_DIR = "strategy_memory/history"
BASE_PATH = "strategy_memory/base_weights.json"
REINFORCE_PATH = "strategy_memory/latest_weights.json"


def load_weights(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def save_snapshot():
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_path = os.path.join(SNAPSHOT_DIR, f"weights_snapshot_{timestamp}.json")

    base = load_weights(BASE_PATH)
    reinforce = load_weights(REINFORCE_PATH)
    final = {k: round(base.get(k, 0) * reinforce.get(k, 1.0), 4) for k in base}

    snapshot = {
        "timestamp": timestamp,
        "base_weights": base,
        "reinforce_weights": reinforce,
        "final_weights": final
    }

    with open(snapshot_path, 'w') as f:
        json.dump(snapshot, f, indent=2)

    print(f"✅ Strategy snapshot saved to {snapshot_path}")
    upload_to_s3(snapshot_path)
    return snapshot_path


if __name__ == '__main__':
    save_snapshot()

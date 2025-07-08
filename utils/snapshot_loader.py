import os
import pandas as pd
import pickle
from datetime import datetime

SNAPSHOT_DIR = "strategy_memory"


def load_latest_snapshot():
    if not os.path.exists(SNAPSHOT_DIR):
        raise FileNotFoundError("strategy_memory folder not found")

    files = [f for f in os.listdir(SNAPSHOT_DIR) if f.endswith('.pkl') or f.endswith('.json')]
    if not files:
        raise FileNotFoundError("No snapshot files found in strategy_memory/")

    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(SNAPSHOT_DIR, f)))
    full_path = os.path.join(SNAPSHOT_DIR, latest_file)

    if latest_file.endswith(".pkl"):
        with open(full_path, 'rb') as f:
            data = pickle.load(f)
    else:
        data = pd.read_json(full_path, typ='series').to_dict()

    return {
        "performance": pd.DataFrame(data.get("strategy_performance", [])),
        "weights": pd.DataFrame(data.get("strategy_weights", [])),
        "status": pd.DataFrame(data.get("strategy_status", [])),
        "raw_path": full_path
    }

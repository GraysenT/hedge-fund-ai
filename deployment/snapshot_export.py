import shutil
import os
from datetime import datetime

SNAPSHOT_DIR = "snapshots"
TIMESTAMP = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
TARGET = os.path.join(SNAPSHOT_DIR, f"snapshot_{TIMESTAMP}")

def export_snapshot():
    os.makedirs(TARGET, exist_ok=True)
    shutil.copy("logs/trades.csv", f"{TARGET}/trades.csv")
    shutil.copy("logs/signals.json", f"{TARGET}/signals.json")
    shutil.copy("strategy_status.json", f"{TARGET}/strategy_status.json")
    print(f"✅ Snapshot saved to {TARGET}")

if __name__ == "__main__":
    export_snapshot()
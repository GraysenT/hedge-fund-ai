import json
import os
from datetime import datetime

LOG_PATH = "logs/self_healing.log"

def log_fault(module, error):
    os.makedirs("logs", exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "module": module,
        "error": str(error)
    }
    try:
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except:
        print("[FaultLog] Failed to write fault log.")

def get_fault_history():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        return [json.loads(line) for line in f.readlines()]
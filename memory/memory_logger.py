import json
from datetime import datetime

def log_memory(event, path="logs/memory_log.json"):
    with open(path, "a") as f:
        f.write(json.dumps({"timestamp": datetime.utcnow().isoformat(), **event}) + "\n")
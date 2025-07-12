import json
import os
from datetime import datetime

MEMORY_LOG = "memory/memory_log.json"

def store_thought(thought):
    os.makedirs("memory", exist_ok=True)
    try:
        with open(MEMORY_LOG, "a") as f:
            f.write(json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "thought": thought
            }) + "\n")
    except Exception as e:
        print(f"[MemoryStore] Error: {e}")
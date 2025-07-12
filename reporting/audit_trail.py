import json
import os
from datetime import datetime
from utils.paths import AUDIT_LOG_FILE

def log_audit(signal, decision, trade=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "signal": signal,
        "decision": decision,
        "trade": trade,
    }

    if not os.path.exists(AUDIT_LOG_FILE):
        with open(AUDIT_LOG_FILE, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(AUDIT_LOG_FILE, "r") as f:
            data = json.load(f)
        data.append(entry)
        with open(AUDIT_LOG_FILE, "w") as f:
            json.dump(data, f, indent=2)
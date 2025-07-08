import json
import os
from datetime import datetime

AUDIT_PATH = "memory/execution_audit.json"

def log_trade(strategy, symbol, action, capital, confidence, approved_by):
    log = {
        "timestamp": datetime.now().isoformat(),
        "strategy": strategy,
        "symbol": symbol,
        "action": action,
        "capital": capital,
        "confidence": confidence,
        "approved_by": approved_by
    }

    if os.path.exists(AUDIT_PATH):
        audit = json.load(open(AUDIT_PATH))
    else:
        audit = []

    audit.append(log)
    with open(AUDIT_PATH, "w") as f:
        json.dump(audit, f, indent=2)

    print("📒 Trade audit logged.")

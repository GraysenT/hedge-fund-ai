import json
import os
from datetime import datetime

AUDIT_DIR = "logs/audit"

def ensure_audit_dir():
    os.makedirs(AUDIT_DIR, exist_ok=True)

def log_audit_event(event_type, details, source="system"):
    """
    Logs a timestamped event into a date-based audit log file.
    
    Args:
        event_type (str): Type of event (e.g., signal_triggered, trade_executed, api_access)
        details (dict): Arbitrary key-value payload describing the event
        source (str): Who/what generated this event (e.g., 'evolve.py', 'api', 'meta_agent')
    """
    ensure_audit_dir()
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    filepath = os.path.join(AUDIT_DIR, f"{date_str}.jsonl")

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "source": source,
        "details": details
    }

    with open(filepath, "a") as f:
        f.write(json.dumps(record) + "\n")

    print(f"🧾 [AUDIT] Logged {event_type} from {source}")

# Example usage
if __name__ == "__main__":
    log_audit_event(
        "signal_triggered",
        {
            "strategy": "stat_arb_v3",
            "action": "SELL",
            "asset": "MSFT",
            "confidence": 0.84
        },
        source="runloop.py"
    )

    log_audit_event(
        "api_access",
        {
            "endpoint": "/api/report",
            "user_role": "viewer",
            "key_id": "key_viewer_abc"
        },
        source="client_api.py"
    )
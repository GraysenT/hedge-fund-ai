import json
from datetime import datetime

REINVENTION_LOG = "logs/reinvention_events.json"

def trigger_reinvention(reason, proposed_change):
    event = {
        "timestamp": datetime.now().isoformat(),
        "reason": reason,
        "proposed_change": proposed_change
    }

    events = []
    try:
        with open(REINVENTION_LOG, "r") as f:
            events = json.load(f)
    except:
        pass

    events.append(event)
    with open(REINVENTION_LOG, "w") as f:
        json.dump(events, f, indent=2)

    return event
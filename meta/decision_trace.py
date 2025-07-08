import json
import os
from datetime import datetime

TRACE_FILE = "meta/decision_trace.json"

def log_decision(decision_type, strategy, reason, impact="medium"):
    trace = json.load(open(TRACE_FILE)) if os.path.exists(TRACE_FILE) else []
    entry = {
        "timestamp": datetime.now().isoformat(),
        "type": decision_type,
        "strategy": strategy,
        "reason": reason,
        "impact": impact
    }
    trace.append(entry)
    with open(TRACE_FILE, "w") as f:
        json.dump(trace, f, indent=2)
    print(f"🧠 Decision logged: {decision_type} - {strategy}")

if __name__ == "__main__":
    log_decision("mutation", "gen_strat_r2_mut4712", "underperformed in current regime", "high")
    
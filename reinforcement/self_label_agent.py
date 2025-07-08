import json
import os
from datetime import datetime

SIGNAL_LOG = "logs/signal_events.json"
LABEL_LOG = "memory/self_labels.json"

def score_strategies_from_labels():
    print("🧠 [Placeholder] Scoring strategies from labels...")
    return []

def update_self_labels():
    if not os.path.exists(SIGNAL_LOG):
        print("⚠️ No signal log to label.")
        return

    with open(SIGNAL_LOG, "r") as f:
        signals = json.load(f)

    labeled = []
    for s in signals[-10:]:
        label = "success" if s.get("confidence", 0) > 0.7 else "fail"
        labeled.append({
            "strategy": s["strategy"],
            "action": s["action"],
            "confidence": s.get("confidence", 0),
            "label": label,
            "timestamp": datetime.utcnow().isoformat()
        })

    os.makedirs("memory", exist_ok=True)
    with open(LABEL_LOG, "w") as f:
        json.dump(labeled, f, indent=2)

    print(f"🔖 Self-labeled {len(labeled)} signals.")

if __name__ == "__main__":
    update_self_labels()
import json
import os
from datetime import datetime

RESEARCH_DB = "memory/research_memory.json"
FEEDBACK_DB = "memory/research_feedback.json"

def integrate_research_feedback():
    if not os.path.exists(RESEARCH_DB):
        return

    with open(RESEARCH_DB, "r") as f:
        memory = json.load(f)

    feedback = []
    for entry in memory:
        feedback.append({
            "id": entry["id"],
            "idea": entry["idea"],
            "score": entry["score"],
            "feedback": "promote" if entry["score"] > 0.75 else "reject",
            "timestamp": datetime.utcnow().isoformat()
        })

    with open(FEEDBACK_DB, "w") as f:
        json.dump(feedback, f, indent=2)

    print(f"📥 Integrated feedback on {len(feedback)} hypotheses.")
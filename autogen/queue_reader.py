import json
QUEUE_FILE = "ultra_frontier_queue.json"

def get_next_phase():
    with open(QUEUE_FILE, "r") as f:
        phases = json.load(f)
    for phase in phases:
        if not phase.get("done"):
            return phase
    return None

def mark_phase_complete(phase_id):
    with open(QUEUE_FILE, "r") as f:
        phases = json.load(f)
    for p in phases:
        if p["id"] == phase_id:
            p["done"] = True
    with open(QUEUE_FILE, "w") as f:
        json.dump(phases, f, indent=2)
import json
from datetime import datetime

TRACKER_PATH = "meta/dev_log.json"

def log_upgrade(name, impact, status="active", notes=""):
    log = json.load(open(TRACKER_PATH)) if os.path.exists(TRACKER_PATH) else []
    entry = {
        "name": name,
        "impact_score": impact,
        "status": status,
        "date": datetime.now().isoformat(),
        "notes": notes
    }
    log.append(entry)
    with open(TRACKER_PATH, "w") as f:
        json.dump(log, f, indent=2)
    print(f"🛠️ Logged: {name}")

def summarize_tracker():
    data = json.load(open(TRACKER_PATH))
    active = [x for x in data if x["status"] == "active"]
    print(f"📈 {len(active)} active upgrades. Highest ROI:")
    for x in sorted(active, key=lambda x: x["impact_score"], reverse=True)[:5]:
        print(f"- {x['name']} (ROI: {x['impact_score']})")

if __name__ == "__main__":
    log_upgrade("Meta Learner", impact=9.1, notes="Boosted regime-awareness by 30%")
    summarize_tracker()
    
import json, os, time
HIST_FILE = "logs/history.json"
os.makedirs("logs", exist_ok=True)

def record_event(event):
    entry = {"timestamp": time.time(), **event}
    data = []
    if os.path.exists(HIST_FILE):
        with open(HIST_FILE) as f:
            data = json.load(f)
    data.append(entry)
    with open(HIST_FILE, "w") as f:
        json.dump(data, f, indent=2)
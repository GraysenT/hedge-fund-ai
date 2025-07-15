import json, os
SEMANTIC_FILE = "logs/semantic_evolution.json"
os.makedirs("logs", exist_ok=True)

def log_language(agent_id, lang):
    entry = {"agent_id": agent_id, "language": lang}
    with open(SEMANTIC_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
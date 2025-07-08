import json
import os
from datetime import datetime

POOL = "federation/shared_plugins/"
VOTES = "federation/plugin_votes.json"

def submit_plugin(name, code):
    os.makedirs(POOL, exist_ok=True)
    path = f"{POOL}{name}.py"
    with open(path, "w") as f:
        f.write(code)
    print(f"📦 Plugin {name} submitted.")

def vote_plugin(name, vote):
    votes = json.load(open(VOTES)) if os.path.exists(VOTES) else {}
    if name not in votes:
        votes[name] = {"up": 0, "down": 0}
    votes[name][vote] += 1
    with open(VOTES, "w") as f:
        json.dump(votes, f, indent=2)
    print(f"🗳 Voted {vote} on {name}.")

if __name__ == "__main__":
    submit_plugin("sma_cross", "def run(): print('BUY if SMA10 > SMA50')")
    vote_plugin("sma_cross", "up")
    
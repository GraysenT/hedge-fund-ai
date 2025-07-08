import os
import json
import uuid
import random

AGENT_DIR = "memory/agents/"
os.makedirs(AGENT_DIR, exist_ok=True)

def create_agent():
    agent_id = f"agent_{uuid.uuid4().hex[:5]}"
    strategies = random.sample([
        "stat_arb", "macro_sentiment", "crypto_edge", "mean_rev", "momentum", "news_spike"
    ], 3)

    profile = {
        "id": agent_id,
        "capital": 1_000_000,
        "strategies": strategies,
        "memory": [],
        "pnl": 0
    }

    with open(f"{AGENT_DIR}/{agent_id}.json", "w") as f:
        json.dump(profile, f, indent=2)

    print(f"🤖 Created virtual agent: {agent_id}")
    return agent_id

def load_agents():
    return [
        json.load(open(os.path.join(AGENT_DIR, f)))
        for f in os.listdir(AGENT_DIR)
        if f.endswith(".json")
    ]

if __name__ == "__main__":
    for _ in range(3):
        create_agent()
import os
import json
from datetime import datetime

TOURNAMENT_PATH = "agents/agent_tournament_results.json"
MEMORY_PATH = "agents/agent_memory.json"

def load_current_results():
    if not os.path.exists(TOURNAMENT_PATH):
        return {}
    with open(TOURNAMENT_PATH) as f:
        return json.load(f)

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH) as f:
            return json.load(f)
    return {}

def update_memory(current, memory):
    date_key = datetime.now().strftime("%Y-%m-%d")
    for agent, stats in current.items():
        if agent not in memory:
            memory[agent] = []
        entry = {
            "date": date_key,
            "pnl": stats["pnl"],
            "days": stats["days"],
            "strategies": stats["strategies"]
        }
        memory[agent].append(entry)
    return memory

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
    print(f"🧠 Agent memory updated → {MEMORY_PATH}")

if __name__ == "__main__":
    current = load_current_results()
    memory = load_memory()
    updated = update_memory(current, memory)
    save_memory(updated)
    
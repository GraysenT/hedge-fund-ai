import json
import os
from datetime import datetime

MEMORY_FILE = "memory/post_existential_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def append_to_memory(entry):
    memory = load_memory()
    memory.append(entry)
    save_memory(memory)
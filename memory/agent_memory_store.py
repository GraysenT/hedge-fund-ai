import json
import os

class AgentMemoryStore:
    def __init__(self, file_path="logs/agent_memory.json"):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save(self, memory):
        with open(self.file_path, "w") as f:
            json.dump(memory, f, indent=2)

    def write_agent_state(self, market: str, state: dict):
        memory = self.load()
        memory[market] = state
        self.save(memory)

    def read_agent_state(self, market: str) -> dict:
        return self.load().get(market, {})
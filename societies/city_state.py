import os
import json

class CityStateNode:
    def __init__(self, market_name):
        self.name = market_name
        self.agent_registry = {}
        self.data_path = f"state/{self.name}.json"
        self.load()

    def load(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                self.agent_registry = json.load(f)

    def save(self):
        with open(self.data_path, "w") as f:
            json.dump(self.agent_registry, f, indent=2)

    def register_agent(self, name, capital=1000):
        self.agent_registry[name] = {"capital": capital, "karma": 0}
        self.save()

    def update_agent(self, name, delta):
        if name in self.agent_registry:
            self.agent_registry[name]["capital"] += delta
            self.save()
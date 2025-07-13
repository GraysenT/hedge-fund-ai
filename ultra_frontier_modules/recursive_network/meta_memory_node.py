import uuid
import json

class MetaMemoryNode:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.memory = []
        self.beliefs = {}

    def receive_insight(self, data):
        self.memory.append(data)
        topic = data.get("topic")
        if topic:
            self.beliefs[topic] = self.beliefs.get(topic, 0) + data.get("confidence", 0.5)

    def export_state(self):
        return {
            "id": self.id,
            "name": self.name,
            "beliefs": self.beliefs,
            "memory": self.memory[-5:]  # Only export recent memory
        }

    def import_state(self, external_state):
        for topic, val in external_state.get("beliefs", {}).items():
            self.beliefs[topic] = (self.beliefs.get(topic, 0) + val) / 2
        for entry in external_state.get("memory", []):
            self.receive_insight(entry)
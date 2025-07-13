import uuid
from datetime import datetime

class SuccessionAgent:
    def __init__(self, name, role, generation=1, memory_blob=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = role  # e.g., "signal scout", "macro reactor"
        self.generation = generation
        self.memory_blob = memory_blob or []
        self.children = []
        self.status = "active"
        self.created_at = datetime.now().isoformat()

    def spawn_child(self, child_name, mutation_notes=""):
        child_memory = self.memory_blob[-5:] + [f"Inherited from {self.name}: {mutation_notes}"]
        child = SuccessionAgent(
            name=child_name,
            role=self.role,
            generation=self.generation + 1,
            memory_blob=child_memory
        )
        self.children.append(child.id)
        return child

    def retire(self, reason):
        self.status = "retired"
        self.retired_reason = reason
        self.retired_at = datetime.now().isoformat()

    def profile(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "generation": self.generation,
            "status": self.status,
            "created": self.created_at,
            "children": self.children,
            "memory": self.memory_blob
        }
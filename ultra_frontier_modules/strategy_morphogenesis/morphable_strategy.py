import uuid
from datetime import datetime

class MorphableStrategy:
    def __init__(self, base_name, base_logic, sensitivity=0.5):
        self.id = str(uuid.uuid4())
        self.name = base_name
        self.base_logic = base_logic  # dictionary of parameters
        self.sensitivity = sensitivity  # 0–1: how easily it morphs
        self.mutation_history = []
        self.last_updated = datetime.now().isoformat()

    def morph(self, memory_event):
        """
        memory_event = {
            "context": "volatility_regime",
            "outcome": "underperformance",
            "adjustment": {"threshold": -0.1}
        }
        """
        for key, delta in memory_event.get("adjustment", {}).items():
            if key in self.base_logic:
                original = self.base_logic[key]
                new_val = original + delta * self.sensitivity
                self.base_logic[key] = round(new_val, 4)
                self.mutation_history.append({
                    "param": key,
                    "from": original,
                    "to": new_val,
                    "context": memory_event["context"],
                    "timestamp": datetime.now().isoformat()
                })
        self.last_updated = datetime.now().isoformat()
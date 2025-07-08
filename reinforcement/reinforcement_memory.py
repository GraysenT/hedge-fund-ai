import json
import time

class ReinforcementMemory:
    def __init__(self, filename="reinforcement_memory.json"):
        self.filename = filename
        self.memory = []

    def record(self, strategy_name, reward, score):
        self.memory.append({
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "strategy": strategy_name,
            "reward": reward,
            "score": score
        })
        self._save()

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def history(self):
        return self.memory
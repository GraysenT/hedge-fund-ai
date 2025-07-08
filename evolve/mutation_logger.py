import json
import time

class MutationLogger:
    def __init__(self, filename="mutation_log.json"):
        self.filename = filename
        self.mutations = []

    def log_mutation(self, new_strategy_name, parent_strategy_name, mutation_details):
        entry = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "strategy": new_strategy_name,
            "parent": parent_strategy_name,
            "details": mutation_details
        }
        self.mutations.append(entry)
        self._save()

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.mutations, f, indent=2)

    def get_all(self):
        return self.mutations
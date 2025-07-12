import json
from datetime import datetime

class StrategyHeritage:
    def __init__(self, storage_file="heritage.json"):
        self.storage_file = storage_file
        self.heritage = {}

    def record_ancestry(self, strategy_name, parent_strategy=None, mutation_notes=None):
        record = {
            "timestamp": datetime.now().isoformat(),
            "parent": parent_strategy,
            "notes": mutation_notes
        }
        if strategy_name not in self.heritage:
            self.heritage[strategy_name] = []

        self.heritage[strategy_name].append(record)
        self._save()

    def _save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.heritage, f, indent=2)

    def view_heritage(self, strategy_name):
        return self.heritage.get(strategy_name, [])

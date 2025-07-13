from collections import defaultdict

class ReputationTracker:
    def __init__(self):
        self.reputation = defaultdict(lambda: {"votes": 0, "wins": 0, "score": 0.0})

    def register_signal(self, node, result):
        self.reputation[node]["votes"] += 1
        if result:
            self.reputation[node]["wins"] += 1
        wins = self.reputation[node]["wins"]
        total = self.reputation[node]["votes"]
        self.reputation[node]["score"] = wins / total if total else 0.0

    def get_rankings(self):
        return sorted(self.reputation.items(), key=lambda x: x[1]["score"], reverse=True)
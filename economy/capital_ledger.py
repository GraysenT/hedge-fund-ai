from collections import defaultdict

class CapitalLedger:
    def __init__(self):
        self.credits = defaultdict(lambda: 1000.0)  # Starting capital

    def update(self, node, pnl):
        self.credits[node] += pnl
        self.credits[node] = max(self.credits[node], 0.0)

    def stake(self, node, amount):
        if self.credits[node] >= amount:
            self.credits[node] -= amount
            return True
        return False

    def leaderboard(self):
        return sorted(self.credits.items(), key=lambda x: x[1], reverse=True)
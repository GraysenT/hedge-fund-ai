from collections import defaultdict

class StrategyPerformance:
    def __init__(self):
        self.stats = defaultdict(lambda: {"pnl": 0.0, "sharpe": 0.0, "trades": 0})

    def update(self, strategy_name: str, pnl: float, sharpe: float):
        self.stats[strategy_name]["pnl"] += pnl
        self.stats[strategy_name]["sharpe"] = sharpe
        self.stats[strategy_name]["trades"] += 1

    def get(self, strategy_name: str):
        return self.stats[strategy_name]

    def all_stats(self):
        return dict(self.stats)
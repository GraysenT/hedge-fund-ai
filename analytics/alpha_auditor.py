class AlphaHealthAuditor:
    def __init__(self):
        self.flags = []

    def audit(self, strategy_metrics):
        for strat, metrics in strategy_metrics.items():
            if metrics['sharpe'] < 0.5:
                self.flags.append((strat, "Low Sharpe Ratio"))
            if metrics['drawdown'] > 0.2:
                self.flags.append((strat, "Excessive Drawdown"))
            if metrics['return'] < 0:
                self.flags.append((strat, "Negative Return"))

        for f in self.flags:
            print(f"[ALPHA AUDIT] {f[0]} flagged: {f[1]}")

        return self.flags
class StrategyPerformanceTracker:
    def __init__(self):
        self.performance_log = []

    def track_strategy_performance(self, strategy_name, pnl, win_rate, sharpe_ratio):
        """Track the performance of a strategy over time."""
        performance_data = {
            "strategy_name": strategy_name,
            "pnl": pnl,
            "win_rate": win_rate,
            "sharpe_ratio": sharpe_ratio
        }
        self.performance_log.append(performance_data)
        print(f"Tracked performance for {strategy_name}: PnL = {pnl}, Win Rate = {win_rate}, Sharpe Ratio = {sharpe_ratio}")
    
    def get_performance_log(self):
        return self.performance_log
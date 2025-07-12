class RecursiveTradeOptimization:
    def __init__(self):
        self.optimized_trades = []

    def optimize_trade(self, trade_id, optimization_factor):
        """Optimize trades recursively for maximum performance."""
        optimized_trade = {"trade_id": trade_id, "optimization_factor": optimization_factor}
        self.optimized_trades.append(optimized_trade)
        print(f"Optimized trade {trade_id} with factor: {optimization_factor}")
    
    def get_optimized_trades(self):
        return self.optimized_trades
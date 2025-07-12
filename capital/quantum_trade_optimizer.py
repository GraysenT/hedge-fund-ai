class QuantumTradeOptimizer:
    def __init__(self):
        self.optimized_trades = []

    def optimize_trade(self, trade_id, quantum_factor):
        """Optimize quantum-based trades recursively."""
        optimized_trade = {"trade_id": trade_id, "quantum_factor": quantum_factor}
        self.optimized_trades.append(optimized_trade)
        print(f"Optimized quantum trade {trade_id} with factor: {quantum_factor}")
    
    def get_optimized_trades(self):
        return self.optimized_trades
class QuantumTradePerformance:
    def __init__(self):
        self.trade_performances = []

    def track_quantum_trade_performance(self, trade_id, performance):
        """Track the performance of trades using quantum strategies."""
        performance_record = {"trade_id": trade_id, "performance": performance}
        self.trade_performances.append(performance_record)
        print(f"Tracked performance for quantum trade {trade_id}: {performance}")
    
    def get_trade_performances(self):
        return self.trade_performances
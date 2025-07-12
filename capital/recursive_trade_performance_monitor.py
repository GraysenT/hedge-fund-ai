class RecursiveTradePerformanceMonitor:
    def __init__(self):
        self.trade_performance = []

    def monitor_trade_performance(self, trade_id, performance):
        """Monitor the performance of trades in alignment with recursive purpose."""
        performance_record = {"trade_id": trade_id, "performance": performance}
        self.trade_performance.append(performance_record)
        print(f"Monitored trade performance: {trade_id} with performance: {performance}")
    
    def get_trade_performance(self):
        return self.trade_performance
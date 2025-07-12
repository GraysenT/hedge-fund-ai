class PerformanceScaling:
    def __init__(self):
        self.performance_data = []

    def scale_performance(self, trade_id, performance_factor):
        """Scale trade performance recursively for long-term optimization."""
        performance = {"trade_id": trade_id, "performance_factor": performance_factor}
        self.performance_data.append(performance)
        print(f"Scaled performance for trade {trade_id} with factor: {performance_factor}")
    
    def get_performance_data(self):
        return self.performance_data
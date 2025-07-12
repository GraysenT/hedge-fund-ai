class MetaStrategyPerformanceTracker:
    def __init__(self):
        self.performance_records = []

    def track_meta_strategy_performance(self, strategy_name, performance_score):
        """Track the performance of each meta-strategy over time."""
        performance_record = {"strategy_name": strategy_name, "performance_score": performance_score}
        self.performance_records.append(performance_record)
        print(f"Tracked performance of meta-strategy {strategy_name}: {performance_score}")
    
    def get_performance_records(self):
        return self.performance_records
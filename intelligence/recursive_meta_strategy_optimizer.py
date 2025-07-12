class RecursiveMetaStrategyOptimizer:
    def __init__(self):
        self.optimized_meta_strategies = []

    def optimize_meta_strategy(self, strategy_name, performance_factor):
        """Optimize meta-strategies recursively for maximum impact."""
        optimized_strategy = {"name": strategy_name, "performance_factor": performance_factor}
        self.optimized_meta_strategies.append(optimized_strategy)
        print(f"Optimized meta-strategy: {strategy_name} with factor: {performance_factor}")
    
    def get_optimized_meta_strategies(self):
        return self.optimized_meta_strategies
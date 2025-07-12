class RecursiveScalingOptimizer:
    def __init__(self):
        self.scaling_strategies = []

    def optimize_scaling(self, strategy_name, scaling_factor):
        """Optimize the recursive scaling of strategies for better performance."""
        scaling_strategy = {"strategy_name": strategy_name, "scaling_factor": scaling_factor}
        self.scaling_strategies.append(scaling_strategy)
        print(f"Optimized scaling for strategy: {strategy_name} with factor: {scaling_factor}")
    
    def get_scaling_strategies(self):
        return self.scaling_strategies
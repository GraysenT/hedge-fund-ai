class DomainSpecificStrategyOptimizer:
    def __init__(self):
        self.optimized_strategies = []

    def optimize_strategy_for_domain(self, strategy_name, domain, optimization_factor):
        """Optimize strategies for specific domains recursively."""
        optimized_strategy = {"strategy_name": strategy_name, "domain": domain, "optimization_factor": optimization_factor}
        self.optimized_strategies.append(optimized_strategy)
        print(f"Optimized strategy: {strategy_name} for domain: {domain} with factor: {optimization_factor}")
    
    def get_optimized_strategies(self):
        return self.optimized_strategies
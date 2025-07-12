class StrategyPropagation:
    def __init__(self):
        self.strategies = []

    def propagate_strategy(self, strategy_name, recursive_factor):
        """Propagate recursive strategies across the system."""
        propagated_strategy = {"name": strategy_name, "factor": recursive_factor}
        self.strategies.append(propagated_strategy)
        print(f"Propagated strategy: {strategy_name} with factor: {recursive_factor}")
    
    def get_propagated_strategies(self):
        return self.strategies
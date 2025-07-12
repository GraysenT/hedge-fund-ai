import random

class RecursiveStrategyGenerator:
    def __init__(self):
        self.generated_strategies = []

    def generate_strategy(self):
        """Generate new recursive strategies based on historical performance."""
        strategy_name = f"Strategy_{random.randint(1, 1000)}"
        performance = random.uniform(0.5, 1.5)  # Random performance metric
        strategy = {"name": strategy_name, "performance": performance}
        self.generated_strategies.append(strategy)
        print(f"Generated strategy: {strategy_name} with performance: {performance}")
    
    def get_generated_strategies(self):
        return self.generated_strategies
class RecursiveStrategyIntegrator:
    def __init__(self):
        self.strategies = []

    def integrate_strategy(self, strategy_name, strategy_details):
        """Integrate recursive strategies into the capital logic."""
        strategy = {"name": strategy_name, "details": strategy_details}
        self.strategies.append(strategy)
        print(f"Integrated strategy: {strategy_name}")
    
    def get_strategies(self):
        return self.strategies
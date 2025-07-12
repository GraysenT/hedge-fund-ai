class RecursiveCapitalStrategy:
    def __init__(self):
        self.strategies = []

    def create_strategy(self, strategy_name):
        """Creates a new recursive capital strategy."""
        strategy = {"name": strategy_name, "status": "active"}
        self.strategies.append(strategy)
        print(f"Created strategy: {strategy_name}")
    
    def get_strategies(self):
        return self.strategies
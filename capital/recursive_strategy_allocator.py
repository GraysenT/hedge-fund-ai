class RecursiveStrategyAllocator:
    def __init__(self):
        self.strategies = []

    def allocate_recursive_strategy(self, strategy_name, allocation_amount):
        """Allocate recursive strategies based on capital scaling and long-term optimization."""
        strategy = {"strategy_name": strategy_name, "allocation_amount": allocation_amount}
        self.strategies.append(strategy)
        print(f"Allocated strategy: {strategy_name} with amount: {allocation_amount}")
    
    def get_allocated_strategies(self):
        return self.strategies
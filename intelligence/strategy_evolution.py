import random

class StrategyEvolution:
    def __init__(self, strategies, performance_tracker):
        self.strategies = strategies  # List of StrategyBase objects
        self.performance_tracker = performance_tracker
        self.reinforced_strategies = []

    def evolve_strategies(self):
        """Evaluate and evolve strategies based on performance."""
        for strategy in self.strategies:
            # Get performance data (from StrategyPerformanceTracker)
            performance_data = self.performance_tracker.get_performance_log()
            strategy_performance = [data for data in performance_data if data['strategy_name'] == strategy.name]
            
            if strategy_performance:
                last_performance = strategy_performance[-1]
                pnl = last_performance['pnl']
                win_rate = last_performance['win_rate']
                sharpe_ratio = last_performance['sharpe_ratio']
                
                # Reinforce profitable strategies
                if pnl > 0 and win_rate > 0.5:  # Example condition: profitable strategies
                    print(f"Reinforcing profitable strategy: {strategy.name}")
                    self.reinforced_strategies.append(strategy)
                    
                    # Reinforce logic (e.g., increase weight or enhance parameters)
                    self.reinforce_strategy(strategy)
                else:
                    print(f"Discarding underperforming strategy: {strategy.name}")
                    # Mutate or remove underperforming strategy (example: discard or mutate)
                    self.mutate_strategy(strategy)

    def reinforce_strategy(self, strategy):
        """Reinforce strategy based on performance (e.g., increase weight)."""
        # Example: Increase the weight of profitable strategies
        strategy.increase_weight()
        print(f"Increased weight of strategy: {strategy.name}")
    
    def mutate_strategy(self, strategy):
        """Mutate or modify strategy parameters for better performance."""
        # Example: Mutate strategy by changing key parameters
        strategy.mutate_parameters()
        print(f"Mutated strategy: {strategy.name}")
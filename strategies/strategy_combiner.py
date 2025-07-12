class StrategyCombiner:
    def __init__(self, strategies):
        self.strategies = strategies  # List of StrategyBase objects

    def combine_signals(self, market_data):
        signals = [strategy.generate_signal(market_data) for strategy in self.strategies]
        
        # Example: Majority voting system (return the signal with the most votes)
        return max(set(signals), key=signals.count)  # Return the signal that appears most frequently
import pandas as pd
from strategies.strategy_base import StrategyBase

class TrendFollowing(StrategyBase):
    def __init__(self, name, moving_average_period=20):
        super().__init__(name)
        self.moving_average_period = moving_average_period

    def generate_signal(self, market_data):
        """Generate trade signal based on the moving average crossover strategy."""
        market_data['SMA'] = market_data['close'].rolling(window=self.moving_average_period).mean()
        last_price = market_data['close'].iloc[-1]
        last_sma = market_data['SMA'].iloc[-1]
        
        if last_price > last_sma:
            return "long"  # Buy signal (price above SMA)
        elif last_price < last_sma:
            return "short"  # Sell signal (price below SMA)
        else:
            return "neutral"  # No clear signal

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for trend following strategy."""
        return (exit_price - entry_price) * position_size  # For a long position
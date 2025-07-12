import pandas as pd
from strategies.strategy_base import StrategyBase

class MeanReversion(StrategyBase):
    def __init__(self, name, moving_average_period=20, threshold=1.5):
        super().__init__(name)
        self.moving_average_period = moving_average_period
        self.threshold = threshold  # The number of standard deviations to use for triggering trades

    def generate_signal(self, market_data):
        """Generate trade signal based on mean reversion strategy."""
        market_data['SMA'] = market_data['close'].rolling(window=self.moving_average_period).mean()
        market_data['std_dev'] = market_data['close'].rolling(window=self.moving_average_period).std()
        last_price = market_data['close'].iloc[-1]
        last_sma = market_data['SMA'].iloc[-1]
        last_std_dev = market_data['std_dev'].iloc[-1]
        
        if last_price < last_sma - (self.threshold * last_std_dev):
            return "long"  # Buy signal (price below mean by a certain threshold)
        elif last_price > last_sma + (self.threshold * last_std_dev):
            return "short"  # Sell signal (price above mean by a certain threshold)
        else:
            return "neutral"  # No signal (price within acceptable range of the mean)

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for mean reversion strategy."""
        return (entry_price - exit_price) * position_size  # For a long position
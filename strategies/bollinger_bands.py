import pandas as pd
from strategies.strategy_base import StrategyBase

class BollingerBands(StrategyBase):
    def __init__(self, name, window=20, num_std_dev=2):
        super().__init__(name)
        self.window = window
        self.num_std_dev = num_std_dev

    def generate_signal(self, market_data):
        """Generate trade signal based on Bollinger Bands strategy."""
        market_data['SMA'] = market_data['close'].rolling(window=self.window).mean()
        market_data['std_dev'] = market_data['close'].rolling(window=self.window).std()
        market_data['upper_band'] = market_data['SMA'] + (self.num_std_dev * market_data['std_dev'])
        market_data['lower_band'] = market_data['SMA'] - (self.num_std_dev * market_data['std_dev'])

        last_price = market_data['close'].iloc[-1]
        last_upper_band = market_data['upper_band'].iloc[-1]
        last_lower_band = market_data['lower_band'].iloc[-1]

        if last_price > last_upper_band:
            return "short"  # Sell signal (price above upper band)
        elif last_price < last_lower_band:
            return "long"  # Buy signal (price below lower band)
        else:
            return "neutral"  # No signal

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for Bollinger Bands strategy."""
        return (exit_price - entry_price) * position_size  # For a long position
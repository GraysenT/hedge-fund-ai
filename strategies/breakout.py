import pandas as pd
from strategies.strategy_base import StrategyBase

class Breakout(StrategyBase):
    def __init__(self, name, lookback_period=20, breakout_threshold=1.05):
        super().__init__(name)
        self.lookback_period = lookback_period
        self.breakout_threshold = breakout_threshold  # e.g., 5% breakout

    def generate_signal(self, market_data):
        """Generate trade signal based on breakout strategy."""
        market_data['high_max'] = market_data['high'].rolling(window=self.lookback_period).max()
        market_data['low_min'] = market_data['low'].rolling(window=self.lookback_period).min()
        
        last_price = market_data['close'].iloc[-1]
        last_high = market_data['high_max'].iloc[-1]
        last_low = market_data['low_min'].iloc[-1]

        if last_price > last_high * self.breakout_threshold:
            return "long"  # Breakout upwards, buy signal
        elif last_price < last_low * self.breakout_threshold:
            return "short"  # Breakdown, sell signal
        else:
            return "neutral"  # No signal

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for breakout strategy."""
        return (exit_price - entry_price) * position_size  # For a long position
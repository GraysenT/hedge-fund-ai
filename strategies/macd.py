import pandas as pd
from strategies.strategy_base import StrategyBase

class MACD(StrategyBase):
    def __init__(self, name, short_window=12, long_window=26, signal_window=9):
        super().__init__(name)
        self.short_window = short_window
        self.long_window = long_window
        self.signal_window = signal_window

    def generate_signal(self, market_data):
        """Generate trade signal based on MACD strategy."""
        market_data['short_ema'] = market_data['close'].ewm(span=self.short_window, adjust=False).mean()
        market_data['long_ema'] = market_data['close'].ewm(span=self.long_window, adjust=False).mean()
        market_data['macd'] = market_data['short_ema'] - market_data['long_ema']
        market_data['signal_line'] = market_data['macd'].ewm(span=self.signal_window, adjust=False).mean()

        last_macd = market_data['macd'].iloc[-1]
        last_signal_line = market_data['signal_line'].iloc[-1]

        if last_macd > last_signal_line:
            return "long"  # Buy signal (MACD crosses above signal line)
        elif last_macd < last_signal_line:
            return "short"  # Sell signal (MACD crosses below signal line)
        else:
            return "neutral"  # No signal

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for MACD strategy."""
        return (exit_price - entry_price) * position_size  # For a long position
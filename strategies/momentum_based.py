import pandas as pd
from strategies.strategy_base import StrategyBase

class MomentumBased(StrategyBase):
    def __init__(self, name, rsi_period=14):
        super().__init__(name)
        self.rsi_period = rsi_period

    def generate_signal(self, market_data):
        """Generate trade signal based on RSI momentum strategy."""
        delta = market_data['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=self.rsi_period).mean()
        avg_loss = loss.rolling(window=self.rsi_period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        last_rsi = rsi.iloc[-1]
        
        if last_rsi > 70:
            return "short"  # Sell signal (overbought market)
        elif last_rsi < 30:
            return "long"  # Buy signal (oversold market)
        else:
            return "neutral"  # No signal (market is neutral)

    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate PnL for momentum-based strategy."""
        return (exit_price - entry_price) * position_size  # For a long position
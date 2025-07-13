import pandas as pd

class Breakout:
    def __init__(self, atr_period=14):
        self.atr_period = atr_period

    def get_signal(self, live_data):
        """Get buy or sell signal based on breakout strategy."""
        prices = live_data["AAPL"]

        # Calculate ATR (Average True Range)
        high_low = prices['high'] - prices['low']
        high_close = abs(prices['high'] - prices['close'].shift())
        low_close = abs(prices['low'] - prices['close'].shift())
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        atr = tr.rolling(window=self.atr_period).mean()

        # Define breakout levels based on ATR
        upper_level = prices['close'].rolling(window=self.atr_period).max() + 2 * atr
        lower_level = prices['close'].rolling(window=self.atr_period).min() - 2 * atr

        # Generate signals based on breakout
        if prices['close'][-1] > upper_level[-1]:
            return "buy"
        elif prices['close'][-1] < lower_level[-1]:
            return "sell"
        return "hold"
    
    def set_params(self, params):
        """Set optimized parameters for the strategy."""
        self.atr_period = params.get('atr_period', self.atr_period)
import pandas as pd

class MeanReversion:
    def __init__(self, lookback_period=20, rsi_period=14):
        self.lookback_period = lookback_period
        self.rsi_period = rsi_period

    def get_signal(self, live_data):
        """Get buy or sell signal based on mean-reversion strategy."""
        prices = live_data["AAPL"]

        # Calculate the rolling mean and standard deviation
        rolling_mean = prices.rolling(window=self.lookback_period).mean()
        rolling_std = prices.rolling(window=self.lookback_period).std()

        # Calculate upper and lower Bollinger Bands
        upper_band = rolling_mean + (rolling_std * 2)
        lower_band = rolling_mean - (rolling_std * 2)

        # Calculate RSI (Relative Strength Index)
        delta = prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=self.rsi_period).mean()
        avg_loss = loss.rolling(window=self.rsi_period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Check conditions for buy/sell signal
        if prices[-1] < lower_band[-1] and rsi[-1] < 30:
            return "buy"
        elif prices[-1] > upper_band[-1] and rsi[-1] > 70:
            return "sell"
        return "hold"
    
    def set_params(self, params):
        """Set optimized parameters for the strategy."""
        self.lookback_period = params.get('lookback_period', self.lookback_period)
        self.rsi_period = params.get('rsi_period', self.rsi_period)
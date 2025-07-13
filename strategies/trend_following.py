import numpy as np
import pandas as pd

class TrendFollowing:
    def __init__(self, moving_average_period=20, ema_period=12):
        self.moving_average_period = moving_average_period
        self.ema_period = ema_period
    
    def get_signal(self, live_data):
        """Get buy or sell signal based on trend-following strategy."""
        prices = live_data["AAPL"]  # Assume live_data has price data for each symbol

        # Calculate simple moving average (SMA)
        sma = prices.rolling(window=self.moving_average_period).mean()
        
        # Calculate exponential moving average (EMA)
        ema = prices.ewm(span=self.ema_period, adjust=False).mean()

        # Calculate MACD
        macd_12 = prices.ewm(span=12, adjust=False).mean()
        macd_26 = prices.ewm(span=26, adjust=False).mean()
        macd = macd_12 - macd_26
        macd_signal = macd.ewm(span=9, adjust=False).mean()

        # Generate signal based on trend
        if prices[-1] > sma[-1] and macd[-1] > macd_signal[-1] and prices[-1] > ema[-1]:
            return "buy"
        elif prices[-1] < sma[-1] and macd[-1] < macd_signal[-1] and prices[-1] < ema[-1]:
            return "sell"
        return "hold"
    
    def set_params(self, params):
        """Set optimized parameters for the strategy."""
        self.moving_average_period = params.get('moving_average_period', self.moving_average_period)
        self.ema_period = params.get('ema_period', self.ema_period)
import pandas as pd
import numpy as np

class VolatilityRegimeDetector:
    def __init__(self, method='atr', window=14):
        self.method = method
        self.window = window

    def classify(self, price_data: pd.DataFrame):
        """
        Classifies volatility regime from price data.
        Args:
            price_data (DataFrame): must have 'close' column
        Returns:
            str: one of ['low_vol', 'normal_vol', 'high_vol']
        """
        if self.method == 'atr':
            return self._classify_by_atr(price_data)
        else:
            raise ValueError(f"Unsupported method: {self.method}")

    def _classify_by_atr(self, df):
        if not {'high', 'low', 'close'}.issubset(df.columns):
            raise ValueError("Data must contain 'high', 'low', 'close' columns for ATR method")

        high = df['high']
        low = df['low']
        close = df['close']
        prev_close = close.shift(1)

        tr = pd.concat([
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs()
        ], axis=1).max(axis=1)

        atr = tr.rolling(window=self.window).mean()
        current_atr = atr.iloc[-1]

        # Use historical percentiles
        past_atrs = atr.dropna()
        low_thresh = np.percentile(past_atrs, 33)
        high_thresh = np.percentile(past_atrs, 66)

        if current_atr < low_thresh:
            return "low_vol"
        elif current_atr > high_thresh:
            return "high_vol"
        else:
            return "normal_vol"

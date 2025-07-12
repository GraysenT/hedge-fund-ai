# strategies/overnight_booster.py

import numpy as np
from scipy.stats import norm

class OvernightBooster:
    def __init__(self, mean_reversion_factor, sniper_factor):
        self.mean_reversion_factor = mean_reversion_factor
        self.sniper_factor = sniper_factor

    def calculate_mean_reversion(self, price_series):
        """
        Calculate mean reversion signal based on price series.
        """
        mean_price = np.mean(price_series)
        return self.mean_reversion_factor * (mean_price - price_series[-1])

    def calculate_sniper(self, price_series):
        """
        Calculate sniper signal based on price series.
        """
        price_change = np.diff(price_series)
        return self.sniper_factor * norm.pdf(price_change)

    def calculate_signals(self, price_series):
        """
        Calculate trading signals based on price series.
        """
        mean_reversion_signal = self.calculate_mean_reversion(price_series)
        sniper_signal = self.calculate_sniper(price_series)

        return mean_reversion_signal + sniper_signal

    def execute_strategy(self, price_series):
        """
        Execute strategy based on price series.
        """
        signals = self.calculate_signals(price_series)

        # Buy if signal is positive, sell if signal is negative
        if signals > 0:
            return 'Buy'
        elif signals < 0:
            return 'Sell'
        else:
            return 'Hold'
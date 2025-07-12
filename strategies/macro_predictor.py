# strategies/macro_predictor.py

import numpy as np

class MacroPredictor:
    def __init__(self, mean_reversion_weight=0.5, scalper_weight=0.5):
        self.mean_reversion_weight = mean_reversion_weight
        self.scalper_weight = scalper_weight

    def mean_reversion(self, price_series):
        mean_price = np.mean(price_series)
        return mean_price - price_series[-1]

    def scalper(self, price_series):
        return price_series[-1] - price_series[-2]

    def predict(self, price_series):
        mean_reversion_signal = self.mean_reversion(price_series)
        scalper_signal = self.scalper(price_series)

        weighted_mean_reversion = self.mean_reversion_weight * mean_reversion_signal
        weighted_scalper = self.scalper_weight * scalper_signal

        return weighted_mean_reversion + weighted_scalper
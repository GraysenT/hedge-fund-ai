# strategies/overnight_signalizer.py

import numpy as np
from scipy.stats import norm

class OvernightSignalizer:
    def __init__(self, mean_reversion_factor, scalping_factor):
        self.mean_reversion_factor = mean_reversion_factor
        self.scalping_factor = scalping_factor

    def calculate_z_score(self, data):
        mean = np.mean(data)
        std_dev = np.std(data)
        return (data - mean) / std_dev

    def mean_reversion_signal(self, data):
        z_scores = self.calculate_z_score(data)
        return -1 * z_scores * self.mean_reversion_factor

    def scalping_signal(self, data):
        return np.sign(np.diff(data)) * self.scalping_factor

    def generate_signals(self, data):
        mean_reversion_signals = self.mean_reversion_signal(data)
        scalping_signals = self.scalping_signal(data)
        return mean_reversion_signals + scalping_signals

    def execute_strategy(self, data):
        signals = self.generate_signals(data)
        return np.where(signals > 0, 'Buy', 'Sell')
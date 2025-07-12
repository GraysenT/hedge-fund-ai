import numpy as np

class VolumeTracker:
    def __init__(self, volatility_threshold, sniper_threshold):
        self.volatility_threshold = volatility_threshold
        self.sniper_threshold = sniper_threshold
        self.volume_history = []

    def update_volume(self, volume):
        self.volume_history.append(volume)

    def calculate_volatility(self):
        return np.std(self.volume_history)

    def is_volatility_high(self):
        return self.calculate_volatility() > self.volatility_threshold

    def is_sniper_behavior(self):
        return self.volume_history[-1] > self.sniper_threshold

    def should_trade(self):
        return self.is_volatility_high() and self.is_sniper_behavior()
# strategies/fed_day_booster.py

import numpy as np

class FedDayBooster:
    def __init__(self, fed_day_signals, predictor):
        self.fed_day_signals = fed_day_signals
        self.predictor = predictor

    def blend_signals(self):
        """
        This function blends the fed_day signals with the predictor behavior.
        """
        blended_signals = np.multiply(self.fed_day_signals, self.predictor.predict())
        return blended_signals

    def update_signals(self, new_signals):
        """
        This function updates the fed_day signals.
        """
        self.fed_day_signals = new_signals

    def update_predictor(self, new_predictor):
        """
        This function updates the predictor.
        """
        self.predictor = new_predictor
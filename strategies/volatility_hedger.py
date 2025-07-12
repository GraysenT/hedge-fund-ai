# strategies/volatility_hedger.py

import numpy as np

class VolatilityHedger:
    def __init__(self, overnight_signals, tracker_behavior):
        self.overnight_signals = overnight_signals
        self.tracker_behavior = tracker_behavior

    def calculate_volatility(self, data):
        return np.std(data)

    def blend_signals(self):
        overnight_volatility = self.calculate_volatility(self.overnight_signals)
        tracker_volatility = self.calculate_volatility(self.tracker_behavior)

        blended_signals = []
        for overnight_signal, tracker_signal in zip(self.overnight_signals, self.tracker_behavior):
            if overnight_volatility > tracker_volatility:
                blended_signals.append(overnight_signal)
            else:
                blended_signals.append(tracker_signal)

        return blended_signals

    def hedge(self, data):
        blended_signals = self.blend_signals()
        hedged_data = []

        for signal, value in zip(blended_signals, data):
            hedged_data.append(value - signal)

        return hedged_data
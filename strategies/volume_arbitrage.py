# strategies/volume_arbitrage.py

import numpy as np
from scipy import stats

class VolumeArbitrage:
    def __init__(self, overnight_signals, signalizer_behavior):
        self.overnight_signals = overnight_signals
        self.signalizer_behavior = signalizer_behavior

    def calculate_signal_strength(self):
        overnight_signals_normalized = self.normalize_signals(self.overnight_signals)
        signalizer_behavior_normalized = self.normalize_signals(self.signalizer_behavior)

        return self.blend_signals(overnight_signals_normalized, signalizer_behavior_normalized)

    @staticmethod
    def normalize_signals(signals):
        return (signals - np.mean(signals)) / np.std(signals)

    @staticmethod
    def blend_signals(signal1, signal2):
        return stats.gmean([signal1, signal2])

if __name__ == "__main__":
    overnight_signals = np.array([1, 2, 3, 4, 5])
    signalizer_behavior = np.array([5, 4, 3, 2, 1])

    volume_arbitrage = VolumeArbitrage(overnight_signals, signalizer_behavior)
    print(volume_arbitrage.calculate_signal_strength())

def generate_signal():
    return 'skip'

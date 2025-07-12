# strategies/crypto_hedger.py

import numpy as np

class CryptoHedger:
    def __init__(self, fed_day_signals, signalizer_behavior):
        self.fed_day_signals = fed_day_signals
        self.signalizer_behavior = signalizer_behavior

    def blend_signals(self):
        blended_signals = []
        for fed_signal, signalizer_signal in zip(self.fed_day_signals, self.signalizer_behavior):
            blended_signal = np.mean([fed_signal, signalizer_signal])
            blended_signals.append(blended_signal)
        return blended_signals

    def execute_strategy(self):
        blended_signals = self.blend_signals()
        for signal in blended_signals:
            if signal > 0:
                self.buy_crypto()
            elif signal < 0:
                self.sell_crypto()

    def buy_crypto(self):
        print("Buying crypto...")

    def sell_crypto(self):
        print("Selling crypto...")
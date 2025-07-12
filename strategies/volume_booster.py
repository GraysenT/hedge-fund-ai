# strategies/volume_booster.py

import numpy as np
from scipy.signal import argrelextrema

class VolumeBooster:
    def __init__(self, data):
        self.data = data
        self.momentum_signals = []
        self.sniper_signals = []

    def calculate_momentum(self, period=14):
        self.data['momentum'] = self.data['close'] - self.data['close'].shift(period)
        self.momentum_signals = self.data['momentum'].tolist()

    def calculate_sniper(self):
        self.data['sniper'] = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        self.sniper_signals = self.data['sniper'].tolist()

    def find_extrema(self, comparator):
        extrema = argrelextrema(np.array(self.momentum_signals), comparator)
        return extrema[0]

    def generate_signals(self):
        self.calculate_momentum()
        self.calculate_sniper()

        buy_signals = self.find_extrema(np.less)
        sell_signals = self.find_extrema(np.greater)

        signals = []
        for i in range(len(self.momentum_signals)):
            if i in buy_signals and self.sniper_signals[i] < self.data['low'][i]:
                signals.append('buy')
            elif i in sell_signals and self.sniper_signals[i] > self.data['high'][i]:
                signals.append('sell')
            else:
                signals.append('hold')

        return signals
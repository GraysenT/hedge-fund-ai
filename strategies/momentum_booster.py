# strategies/momentum_booster.py

import pandas as pd
from scipy.signal import argrelextrema

class MomentumBooster:
    def __init__(self, data):
        self.data = data

    def calculate_momentum(self):
        self.data['Momentum'] = self.data['Close'] - self.data['Close'].shift(10)

    def calculate_volume_signals(self):
        self.data['Volume_Signal'] = self.data['Volume'].pct_change()

    def scalper_behavior(self):
        self.data['Scalper_Signal'] = self.data['High'] - self.data['Low']

    def generate_signals(self):
        self.calculate_momentum()
        self.calculate_volume_signals()
        self.scalper_behavior()

        self.data['Buy_Signal'] = ((self.data['Momentum'] > 0) & 
                                   (self.data['Volume_Signal'] > 0) & 
                                   (self.data['Scalper_Signal'] > 0))

        self.data['Sell_Signal'] = ((self.data['Momentum'] < 0) & 
                                    (self.data['Volume_Signal'] < 0) & 
                                    (self.data['Scalper_Signal'] < 0))

        return self.data

    def execute_strategy(self):
        signals = self.generate_signals()
        buy_signals = signals[signals['Buy_Signal'] == True]
        sell_signals = signals[signals['Sell_Signal'] == True]

        return buy_signals, sell_signals
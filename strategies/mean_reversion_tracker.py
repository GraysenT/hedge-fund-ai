import numpy as np
import pandas as pd
from scipy.stats import norm

class MeanReversionTracker:
    def __init__(self, lookback, z_score_threshold):
        self.lookback = lookback
        self.z_score_threshold = z_score_threshold

    def generate_signals(self, price_data):
        signals = pd.DataFrame(index=price_data.index)
        signals['price'] = price_data

        signals['mean'] = signals['price'].rolling(window=self.lookback).mean()
        signals['std'] = signals['price'].rolling(window=self.lookback).std()
        signals['z_score'] = (signals['price'] - signals['mean']) / signals['std']

        signals['long_entry'] = signals['z_score'] < -self.z_score_threshold
        signals['short_entry'] = signals['z_score'] > self.z_score_threshold
        signals['long_exit'] = signals['z_score'] >= 0
        signals['short_exit'] = signals['z_score'] <= 0

        signals['positions_long'] = np.nan
        signals.loc[signals['long_entry'],'positions_long'] = 1
        signals.loc[signals['long_exit'],'positions_long'] = 0

        signals['positions_short'] = np.nan
        signals.loc[signals['short_entry'],'positions_short'] = -1
        signals.loc[signals['short_exit'],'positions_short'] = 0

        signals = signals.fillna(method='ffill')
        signals['positions'] = signals['positions_long'] + signals['positions_short']

        return signals

def generate_signal():
    return 'skip'

import numpy as np
import pandas as pd
from scipy import stats

class MeanReversionSignalizer:
    def __init__(self, lookback, z_score_threshold):
        self.lookback = lookback
        self.z_score_threshold = z_score_threshold

    def generate_signals(self, price_series):
        signals = pd.DataFrame(index=price_series.index)
        signals['price'] = price_series

        signals['moving_average'] = signals['price'].rolling(window=self.lookback).mean()
        signals['moving_std_dev'] = signals['price'].rolling(window=self.lookback).std()
        signals['z_score'] = (signals['price'] - signals['moving_average']) / signals['moving_std_dev']

        signals['signal'] = 0
        signals.loc[signals['z_score'] > self.z_score_threshold, 'signal'] = -1
        signals.loc[signals['z_score'] < -self.z_score_threshold, 'signal'] = 1

        return signals

class Scalper:
    def __init__(self, threshold):
        self.threshold = threshold

    def generate_signals(self, price_series):
        signals = pd.DataFrame(index=price_series.index)
        signals['price'] = price_series

        signals['return'] = signals['price'].pct_change()
        signals['signal'] = 0
        signals.loc[signals['return'] > self.threshold, 'signal'] = -1
        signals.loc[signals['return'] < -self.threshold, 'signal'] = 1

        return signals

class MeanReversionScalperStrategy:
    def __init__(self, lookback, z_score_threshold, scalper_threshold):
        self.mean_reversion_signalizer = MeanReversionSignalizer(lookback, z_score_threshold)
        self.scalper = Scalper(scalper_threshold)

    def generate_signals(self, price_series):
        mean_reversion_signals = self.mean_reversion_signalizer.generate_signals(price_series)
        scalper_signals = self.scalper.generate_signals(price_series)

        signals = pd.DataFrame(index=price_series.index)
        signals['signal'] = np.where(mean_reversion_signals['signal'] == scalper_signals['signal'],
                                      mean_reversion_signals['signal'], 0)

        return signals

def generate_signal():
    return 'skip'

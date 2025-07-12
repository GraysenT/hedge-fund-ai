# strategies/mean_reversion_scalper.py

import numpy as np
from scipy.stats import norm

class MeanReversionScalper:
    def __init__(self, window_size, num_std):
        self.window_size = window_size
        self.num_std = num_std

    def calculate_z_score(self, series):
        mean = series.rolling(window=self.window_size).mean()
        std_dev = series.rolling(window=self.window_size).std()
        z_score = (series - mean) / std_dev
        return z_score

    def generate_signals(self, price_data):
        z_scores = self.calculate_z_score(price_data)

        signals = pd.DataFrame(index=price_data.index)
        signals['long_entry'] = z_scores < -self.num_std
        signals['short_entry'] = z_scores > self.num_std
        signals['long_exit'] = z_scores >= 0
        signals['short_exit'] = z_scores <= 0

        return signals

    def execute_trades(self, price_data, initial_balance, transaction_cost):
        signals = self.generate_signals(price_data)

        positions = pd.DataFrame(index=signals.index).fillna(0.0)
        portfolio = pd.DataFrame(index=signals.index).fillna(0.0)

        positions['long'] = np.where(signals['long_entry'], 1, np.nan)
        positions['short'] = np.where(signals['short_entry'], -1, np.nan)

        positions['long'].fillna(method='ffill', inplace=True)
        positions['short'].fillna(method='ffill', inplace=True)

        positions['long'].fillna(0, inplace=True)
        positions['short'].fillna(0, inplace=True)

        portfolio['positions'] = positions['long'] + positions['short']
        portfolio['cash'] = initial_balance - (positions.diff() * price_data).cumsum() - transaction_cost
        portfolio['total'] = portfolio['cash'] + (portfolio['positions'] * price_data).cumsum()

        return portfolio

def generate_signal():
    return 'skip'

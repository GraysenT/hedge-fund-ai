# strategies/overnight_arbitrage.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class OvernightArbitrage:
    def __init__(self, volume_threshold=1000, predictor_threshold=0.5):
        self.volume_threshold = volume_threshold
        self.predictor_threshold = predictor_threshold
        self.model = RandomForestRegressor()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def execute_strategy(self, data):
        """
        Execute the strategy on the given data.

        The data is a DataFrame with columns: 'volume', 'predictor', 'price'
        """
        # Filter rows where volume is greater than the threshold
        volume_signals = data[data['volume'] > self.volume_threshold]

        # Filter rows where predictor is greater than the threshold
        predictor_signals = volume_signals[volume_signals['predictor'] > self.predictor_threshold]

        # If there are no signals, do nothing
        if predictor_signals.empty:
            return []

        # Train the model on the signals
        X = predictor_signals[['volume', 'predictor']]
        y = predictor_signals['price']
        self.fit(X, y)

        # Predict the price for the next day
        next_day_volume = data.iloc[-1]['volume']
        next_day_predictor = data.iloc[-1]['predictor']
        next_day_price = self.predict([[next_day_volume, next_day_predictor]])

        # If the predicted price is greater than the current price, buy
        if next_day_price > data.iloc[-1]['price']:
            return [('buy', next_day_price)]
        else:
            return [('sell', next_day_price)]
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class FedDaySignalizer:
    def __init__(self, momentum_period=14, prediction_period=5):
        self.momentum_period = momentum_period
        self.prediction_period = prediction_period
        self.model = LinearRegression()

    def calculate_momentum(self, data):
        return data - data.shift(self.momentum_period)

    def train_predictor(self, data):
        X = np.arange(len(data)).reshape(-1, 1)
        y = data.values
        self.model.fit(X, y)

    def predict_behavior(self, days):
        X = np.arange(days).reshape(-1, 1)
        return self.model.predict(X)

    def generate_signals(self, data):
        momentum = self.calculate_momentum(data)
        self.train_predictor(momentum.dropna())
        prediction = self.predict_behavior(self.prediction_period)
        signal = pd.Series(prediction, index=np.arange(len(data), len(data) + self.prediction_period))
        return signal
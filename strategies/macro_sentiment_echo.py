# strategies/macro_sentiment_echo.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class MacroSentimentEcho:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        return self.scaler.transform(data)

    def fit(self, X, y):
        X = self.preprocess_data(X)
        self.model.fit(X, y)

    def predict(self, X):
        X = self.preprocess_data(X)
        return self.model.predict(X)

    def evaluate(self, X, y):
        X = self.preprocess_data(X)
        y_pred = self.model.predict(X)
        accuracy = np.mean(y_pred == y)
        return accuracy
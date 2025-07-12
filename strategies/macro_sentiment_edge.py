# strategies/macro_sentiment_edge.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class MacroSentimentEdge:
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.model = RandomForestClassifier()

    def preprocess_data(self):
        self.data = self.data.fillna(self.data.mean())
        self.data = (self.data - self.data.min()) / (self.data.max() - self.data.min())
        return self.data

    def split_data(self, test_size=0.2):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data, self.target, test_size=test_size, random_state=42)
        return self.X_train, self.X_test, self.y_train, self.y_test

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, new_data):
        return self.model.predict(new_data)

    def evaluate_model(self):
        return self.model.score(self.X_test, self.y_test)

    def run(self):
        self.preprocess_data()
        self.split_data()
        self.train_model()
        return self.evaluate_model()
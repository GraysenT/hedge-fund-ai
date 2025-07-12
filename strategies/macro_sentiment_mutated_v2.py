import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

class MacroSentimentMutatedV2:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def preprocess_data(self):
        self.data.dropna(inplace=True)
        self.data['sentiment_score'] = self.data['sentiment_score'].apply(lambda x: 1 if x > 0 else 0)
        self.X = self.data.drop('sentiment_score', axis=1)
        self.y = self.data['sentiment_score']

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred)

    def predict(self, new_data):
        return self.model.predict(new_data)

def generate_signal():
    # TEMP MOCK DATA
    data = pd.DataFrame({
        "sentiment_score": [random.uniform(-1, 1) for _ in range(100)],
        "macro_score": [random.uniform(-1, 1) for _ in range(100)],
        "volume": [random.randint(100, 10000) for _ in range(100)],
    })

    model = MacroSentimentMutatedV2(data)
    model.preprocess_data()
    model.split_data()
    model.train_model()

    # Prediction logic
    test_input = pd.DataFrame([{
        "sentiment_score": 0.5,
        "macro_score": 0.4,
        "volume": 5000
    }])

    pred = model.predict(test_input)[0]
    return "buy" if pred == 1 else "sell"
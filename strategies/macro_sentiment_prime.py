# strategies/macro_sentiment_prime.py

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

class MacroSentimentPrime:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def preprocess_data(self, data):
        processed_data = data.copy()
        processed_data['text'] = processed_data['text'].str.lower()
        return processed_data

    def fit(self, data, target):
        self.vectorizer = CountVectorizer(stop_words='english')
        self.model = LogisticRegression()

        pipeline = Pipeline([
            ('vectorizer', self.vectorizer),
            ('classifier', self.model)
        ])

        train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

        pipeline.fit(train_data, train_target)

        predictions = pipeline.predict(test_data)

        print("Classification Report:\n", classification_report(test_target, predictions))
        print("Accuracy Score: ", accuracy_score(test_target, predictions))

        self.model = pipeline

    def predict(self, data):
        if self.model is None:
            raise Exception("Model not trained yet. Call 'fit' with appropriate arguments before predicting.")
        return self.model.predict(data)

    def save_model(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, file_path):
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)

def generate_signal():
    return 'skip'

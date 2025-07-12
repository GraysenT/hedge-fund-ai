# strategies/macro_sentiment_reborn.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class MacroSentimentReborn:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def process_data(self, data):
        if isinstance(data, pd.DataFrame):
            data['sentiment'] = data['text'].apply(self.analyze_sentiment)
        else:
            raise ValueError("Data should be a pandas DataFrame")
        return data

    def analyze_sentiment(self, text):
        sentiment_score = self.analyzer.polarity_scores(text)
        return sentiment_score['compound']

    def get_macro_sentiment(self, data):
        processed_data = self.process_data(data)
        macro_sentiment = processed_data['sentiment'].mean()
        return macro_sentiment
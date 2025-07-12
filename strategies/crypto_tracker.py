# File: strategies/crypto_tracker.py

import requests
import time
from datetime import datetime, timedelta

class CryptoTracker:
    def __init__(self, symbol, interval='1h'):
        self.symbol = symbol
        self.interval = interval
        self.base_url = f'https://api.binance.com/api/v3'
        self.scalper_behavior = False

    def get_klines(self):
        endpoint = f'{self.base_url}/klines'
        params = {
            'symbol': self.symbol,
            'interval': self.interval
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data

    def analyze_data(self, data):
        closing_prices = [float(item[4]) for item in data]
        average_price = sum(closing_prices) / len(closing_prices)
        latest_price = closing_prices[-1]
        if latest_price > average_price:
            self.scalper_behavior = True
        else:
            self.scalper_behavior = False

    def run(self):
        while True:
            data = self.get_klines()
            self.analyze_data(data)
            if self.scalper_behavior:
                print(f'{self.symbol} is bullish, consider buying.')
            else:
                print(f'{self.symbol} is bearish, consider selling.')
            time.sleep(60 * 60)  # sleep for an hour

if __name__ == "__main__":
    tracker = CryptoTracker('BTCUSDT')
    tracker.run()
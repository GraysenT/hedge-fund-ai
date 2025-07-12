# File: strategies/crypto_arbitrage.py

import requests
from datetime import datetime, timedelta

class CryptoArbitrage:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.crypto.com/v1/"
        self.headers = {
            "Content-Type": "application/json",
            "X-MBX-APIKEY": self.api_key
        }

    def get_ticker_price(self, symbol):
        url = self.base_url + f"ticker/price?symbol={symbol}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_macro_signals(self, symbol):
        url = self.base_url + f"klines?symbol={symbol}&interval=1d"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        signals = []
        for kline in data:
            open_time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore = kline
            if float(close) > float(open):
                signals.append("buy")
            else:
                signals.append("sell")
        return signals

    def get_signalizer_behavior(self, symbol, start_time, end_time):
        url = self.base_url + f"aggTrades?symbol={symbol}&startTime={start_time}&endTime={end_time}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        behavior = []
        for trade in data:
            if trade['isBuyerMaker']:
                behavior.append("buy")
            else:
                behavior.append("sell")
        return behavior

    def execute_strategy(self, symbol):
        current_price = self.get_ticker_price(symbol)
        macro_signals = self.get_macro_signals(symbol)
        start_time = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
        end_time = int(datetime.now().timestamp() * 1000)
        signalizer_behavior = self.get_signalizer_behavior(symbol, start_time, end_time)

        if macro_signals.count("buy") > macro_signals.count("sell") and signalizer_behavior.count("buy") > signalizer_behavior.count("sell"):
            return "buy"
        elif macro_signals.count("sell") > macro_signals.count("buy") and signalizer_behavior.count("sell") > signalizer_behavior.count("buy"):
            return "sell"
        else:
            return "hold"

def generate_signal():
    return 'skip'

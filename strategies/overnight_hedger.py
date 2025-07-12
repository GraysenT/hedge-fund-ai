import numpy as np

class OvernightHedger:
    def __init__(self, volume_threshold=1000, arbitrage_threshold=0.01):
        self.volume_threshold = volume_threshold
        self.arbitrage_threshold = arbitrage_threshold

    def calculate_arbitrage(self, buy_price, sell_price):
        return (sell_price - buy_price) / buy_price

    def should_trade(self, volume, buy_price, sell_price):
        arbitrage = self.calculate_arbitrage(buy_price, sell_price)
        return volume > self.volume_threshold and arbitrage > self.arbitrage_threshold

    def execute_trade(self, volume, buy_price, sell_price):
        if self.should_trade(volume, buy_price, sell_price):
            return 'Execute Trade'
        else:
            return 'Do Not Execute Trade'
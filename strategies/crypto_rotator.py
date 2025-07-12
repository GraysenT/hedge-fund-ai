# File: strategies/crypto_rotator.py
# Description: A strategy that blends volatility signals with scalper behavior.

import numpy as np
from scipy.stats import norm

class CryptoRotator:
    def __init__(self, initial_investment=10000):
        self.initial_investment = initial_investment
        self.current_investment = initial_investment
        self.crypto_portfolio = {}

    def volatility_signal(self, price_data):
        log_returns = np.log(1 + price_data.pct_change())
        volatility = log_returns.std() * np.sqrt(252)
        return volatility

    def scalper_behavior(self, price_data, volatility):
        z_score = (price_data - price_data.rolling(window=20).mean()) / price_data.rolling(window=20).std()
        buy_signal = z_score < -1
        sell_signal = z_score > 1
        return buy_signal, sell_signal

    def execute_strategy(self, price_data):
        volatility = self.volatility_signal(price_data)
        buy_signal, sell_signal = self.scalper_behavior(price_data, volatility)

        for i in range(len(price_data)):
            if buy_signal[i] and self.current_investment > 0:
                self.crypto_portfolio[i] = self.current_investment / price_data[i]
                self.current_investment = 0
            elif sell_signal[i] and i in self.crypto_portfolio:
                self.current_investment = self.crypto_portfolio[i] * price_data[i]
                del self.crypto_portfolio[i]

        return self.current_investment
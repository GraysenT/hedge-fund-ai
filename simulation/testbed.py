import pandas as pd
import yfinance as yf
from strategies.lstm_core import LSTMStrategy

symbol = "AAPL"
data = yf.download(symbol, period="2y", interval="1d")
prices = data['Close']
prices.name = symbol

strategy = LSTMStrategy()
strategy.train(prices)
signal = strategy.predict(prices)

print("[SIMULATION RESULT]")
print(signal)
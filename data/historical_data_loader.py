import yfinance as yf
import pandas as pd

def get_data(symbol: str, period="1y", interval="1d") -> pd.DataFrame:
    df = yf.download(symbol, period=period, interval=interval)
    df["ma"] = df["Close"].rolling(window=20).mean()
    df["upper_band"] = df["ma"] + 2 * df["Close"].rolling(window=20).std()
    df["lower_band"] = df["ma"] - 2 * df["Close"].rolling(window=20).std()
    df["recent_high"] = df["High"].rolling(window=10).max()
    df["recent_low"] = df["Low"].rolling(window=10).min()
    return df
import pandas as pd

def enrich_data(df):
    """Add technical indicators and basic sentiment tags."""
    df = df.copy()
    if "Close" in df:
        df["SMA_20"] = df["Close"].rolling(window=20).mean()
        df["SMA_50"] = df["Close"].rolling(window=50).mean()
        df["Momentum"] = df["Close"].diff(5)
        df["Volatility"] = df["Close"].rolling(window=10).std()

    df.dropna(inplace=True)
    return df

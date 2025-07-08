import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import zscore
from statsmodels.tsa.stattools import coint

def get_price_data(tickers, start="2023-01-01"):
    """
    Download adjusted close prices for a list of tickers.
    Supports both single and multiple tickers.
    """
    raw = yf.download(tickers, start=start, group_by="ticker", auto_adjust=False)

    if len(tickers) == 1:
        ticker = tickers[0]
        df = raw["Adj Close"].to_frame(name=ticker)
    else:
        try:
            df = pd.concat([raw[ticker]["Adj Close"].rename(ticker) for ticker in tickers], axis=1)
        except KeyError:
            raise ValueError("❌ 'Adj Close' not found in downloaded data. Check ticker symbols or retry.")

    return df.dropna()

def find_cointegrated_pairs(price_df, threshold=0.05):
    """
    Find statistically cointegrated pairs of assets using the Engle-Granger test.
    """
    pairs = []
    tickers = price_df.columns
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            s1 = price_df[tickers[i]]
            s2 = price_df[tickers[j]]
            _, pval, _ = coint(s1, s2)
            if pval < threshold:
                pairs.append((tickers[i], tickers[j], pval))
    return pairs

def calculate_spread_zscore(s1, s2):
    """
    Calculate the spread and z-score between two price series.
    """
    spread = s1 - s2
    z = zscore(spread)
    return z, spread
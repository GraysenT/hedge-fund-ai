import yfinance as yf
import pandas as pd
from datetime import datetime

def generate_volatility_signals(tickers=["SPY", "QQQ"], lookback=20):
    signals = []
    for ticker in tickers:
        data = yf.download(ticker, period="60d", interval="1d")
        if data.empty or len(data) < lookback:
            continue

        data["return"] = data["Adj Close"].pct_change()
        vol = data["return"].rolling(window=lookback).std().iloc[-1]

        if vol > 0.03:
            signals.append({
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "strategy": "volatility_spike",
                "ticker": ticker,
                "signal": "hedge with puts",
                "confidence": min(vol * 10, 1.0),
                "vol": vol
            })
        elif vol < 0.01:
            signals.append({
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "strategy": "volatility_crush",
                "ticker": ticker,
                "signal": "sell options premium",
                "confidence": 1.0 - vol * 10,
                "vol": vol
            })

    return pd.DataFrame(signals)
    

def generate_signal():
    return 'skip'

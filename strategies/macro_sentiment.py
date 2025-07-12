def generate_macro_sentiment_signal(ticker, price):
    action = "BUY" if price > 400 else "HOLD"
    return {
        "timestamp": None,
        "asset": ticker,
        "strategy": "macro_sentiment",
        "price": price,
        "action": action,
        "confidence": 0.91
    }

def generate_signal():
    return "buy"
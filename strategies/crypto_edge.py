def generate_crypto_signal(ticker, price):
    action = "BUY" if price < 25000 else "HOLD"
    return {
        "timestamp": None,
        "asset": ticker,
        "strategy": "crypto_edge",
        "price": price,
        "action": action,
        "confidence": 0.87
    }

def generate_signal():
    return 'skip'

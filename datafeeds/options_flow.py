def fetch_unusual_options():
    # Mock for now; real source like Barchart or Market Chameleon can be added
    return [
        {"symbol": "AAPL", "type": "CALL", "strike": 200, "vol": 3.2, "sentiment": "bullish"},
        {"symbol": "TSLA", "type": "PUT", "strike": 650, "vol": 5.1, "sentiment": "bearish"},
    ]
import json
import os

MACRO_LOG = "memory/macro_regime.json"

def route_intermarket_signals(signal):
    if not os.path.exists(MACRO_LOG):
        return signal

    with open(MACRO_LOG) as f:
        macro = json.load(f)

    if macro["macro_regime"] == "Stagflation":
        signal["hedge"] = "Gold Futures"
    elif macro["macro_regime"] == "Reflation":
        signal["hedge"] = "Equity Index Long"
    elif macro["macro_regime"] == "Recession Risk":
        signal["hedge"] = "Bond ETF Long"

    print(f"🧭 Routed signal with macro-aware hedge: {signal}")
    return signal

if __name__ == "__main__":
    sample_signal = {"strategy": "macro_sentiment", "action": "BUY", "asset": "SPY"}
    route_intermarket_signals(sample_signal)
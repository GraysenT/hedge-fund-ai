import json
import random

def load_public_signals():
    # Simulated external feed (could be scraped or subscribed)
    return [
        {"symbol": "AAPL", "action": "buy", "confidence": 0.78},
        {"symbol": "TSLA", "action": "sell", "confidence": 0.65}
    ]

def merge_signals(internal, external):
    all_signals = internal + external
    combined = {}
    for s in all_signals:
        symbol = s["symbol"]
        weight = s["confidence"]
        if symbol not in combined:
            combined[symbol] = {"buy": 0, "sell": 0}
        combined[symbol][s["action"]] += weight

    print("🔄 Merged Signal View:")
    for sym, scores in combined.items():
        action = "buy" if scores["buy"] > scores["sell"] else "sell"
        print(f"{sym} → {action.upper()} (Score: {round(scores[action], 2)})")

if __name__ == "__main__":
    internal = [{"symbol": "AAPL", "action": "buy", "confidence": 0.91}]
    external = load_public_signals()
    merge_signals(internal, external)
    
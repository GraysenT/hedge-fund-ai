import json
from collections import defaultdict

def gather_signals():
    # Simulated inputs from 3 nodes
    proposals = [
        [{"symbol": "TSLA", "action": "buy", "confidence": 0.91}],
        [{"symbol": "TSLA", "action": "buy", "confidence": 0.87}],
        [{"symbol": "TSLA", "action": "sell", "confidence": 0.6}]
    ]

    votes = defaultdict(lambda: {"buy": 0, "sell": 0})
    for node_signals in proposals:
        for sig in node_signals:
            votes[sig["symbol"]][sig["action"]] += sig["confidence"]

    print("🗳 Consensus Voting:")
    for symbol, results in votes.items():
        action = "buy" if results["buy"] > results["sell"] else "sell"
        print(f"{symbol} → {action.upper()} (BUY: {round(results['buy'],2)}, SELL: {round(results['sell'],2)})")

if __name__ == "__main__":
    gather_signals()
    
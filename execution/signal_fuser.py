import random

def get_signals(symbol):
    return {
        "lstm": {"action": "buy", "confidence": random.uniform(0.7, 0.9)},
        "cnn": {"action": "buy", "confidence": random.uniform(0.6, 0.85)},
        "transformer": {"action": "hold", "confidence": random.uniform(0.5, 0.75)},
        "plugin": {"action": "buy", "confidence": random.uniform(0.6, 0.95)}
    }

def fuse(signals):
    vote = {}
    for model, data in signals.items():
        vote[data["action"]] = vote.get(data["action"], 0) + data["confidence"]

    final = max(vote, key=vote.get)
    confidence = round(vote[final] / sum(vote.values()), 4)
    return final, confidence

if __name__ == "__main__":
    symbol = "TSLA"
    sigs = get_signals(symbol)
    action, conf = fuse(sigs)
    print(f"🎯 Final Signal for {symbol}: {action.upper()} (Confidence: {conf})")
    
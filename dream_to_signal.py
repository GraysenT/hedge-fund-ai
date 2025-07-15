def interpret_dream(dream):
    future = dream["future_price"]
    now = dream["context"]["price"]
    if future > now * 1.01:
        return "buy"
    elif future < now * 0.99:
        return "sell"
    return "hold"
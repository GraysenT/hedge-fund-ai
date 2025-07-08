import random

def load_price_feature():
    return random.uniform(-1, 1)

def load_news_sentiment():
    return random.uniform(-0.5, 0.5)

def interpret_voice_command():
    return random.choice(["buy", "hold", "sell"])

def fusion():
    p = load_price_feature()
    n = load_news_sentiment()
    v = interpret_voice_command()

    total = p + n + (1 if v == "buy" else -1 if v == "sell" else 0)
    signal = "BUY" if total > 0.5 else "SELL" if total < -0.5 else "HOLD"
    print(f"🧠 Foundation Signal: {signal} | Score: {round(total, 3)}")

if __name__ == "__main__":
    fusion()
    
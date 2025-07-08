import random


def run():
    print("🧠 Running Commodity AI Forecast...")

    commodities = ["Gold", "Oil", "Wheat", "Cattle"]
    for asset in commodities:
        signal = random.choice(["Buy", "Sell", "Hold"])
        confidence = round(random.uniform(0.6, 0.95), 2)
        print(f" → {asset}: {signal} (Confidence: {confidence})")

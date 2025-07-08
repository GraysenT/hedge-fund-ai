import pandas as pd
import os

def compute_atr(symbol):
    path = f"data/price_history/{symbol}.csv"
    if not os.path.exists(path):
        return 0
    df = pd.read_csv(path)
    df["hl"] = df["high"] - df["low"]
    return round(df["hl"].rolling(5).mean().iloc[-1], 2)

def rank_by_volatility(symbols):
    ranked = []
    for s in symbols:
        atr = compute_atr(s)
        ranked.append((s, atr))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked[:20]

if __name__ == "__main__":
    from data.symbol_universe import get_universe
    top = rank_by_volatility(get_universe())
    print("⚡ Most volatile tradable symbols:")
    for s, atr in top:
        print(f"{s}: ATR {atr}")
    
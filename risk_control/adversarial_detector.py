import pandas as pd
import os

def detect_spoofing(symbol):
    path = f"data/price_history/{symbol}.csv"
    if not os.path.exists(path):
        return []

    df = pd.read_csv(path)
    df["gap"] = df["close"].pct_change().fillna(0)
    df["reverse"] = df["gap"] * df["gap"].shift(-1)

    reversals = df[df["reverse"] < -0.0005]
    spikes = df[df["gap"].abs() > 0.03]

    combined = pd.merge(reversals, spikes, how="inner", on="timestamp")
    return combined["timestamp"].tolist()

if __name__ == "__main__":
    flagged = detect_spoofing("TSLA")
    print(f"⚠️ Spoofing patterns detected at: {flagged}")

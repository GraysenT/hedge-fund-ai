import csv
import os
import datetime

def run():
    print("\n🧠 Signal Fusion Engine (Phase 2) Running...")

    # Simulated input scores (normally from LSTM, sentiment, macro, etc.)
    lstm_forecast = {
        "Gold": 0.78,
        "Oil": 0.61,
        "Wheat": 0.73,
        "Cattle": 0.69,
    }

    sentiment_scores = {
        "Gold": 0.7,
        "Oil": 0.4,
        "Wheat": 0.8,
        "Cattle": 0.6,
    }

    macro_signals = {
        "Gold": 1.0,
        "Oil": 0.5,
        "Wheat": 0.6,
        "Cattle": 0.4,
    }

    fused_scores = {}
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_rows = []

    for asset in lstm_forecast:
        fused_score = round((
            0.5 * lstm_forecast[asset] +
            0.3 * sentiment_scores[asset] +
            0.2 * macro_signals[asset]
        ), 2)
        signal = "Buy" if fused_score >= 0.7 else "Hold" if fused_score >= 0.5 else "Sell"
        fused_scores[asset] = fused_score

        print(f" → {asset}: {signal} (Fused Confidence: {fused_score})")

        # Add strategy name to the log
        log_rows.append([today, asset, signal, fused_score, "Fusion"])

    # Save to CSV log
    log_path = os.path.join("logs", "signal_log.csv")
    file_exists = os.path.isfile(log_path)

    with open(log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Asset", "Signal", "Confidence", "Strategy"])
        writer.writerows(log_rows)

    print(f"📘 Signals logged to {log_path}")
    
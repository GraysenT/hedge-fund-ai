import pandas as pd
import os

# Create /data directory if missing
os.makedirs("data", exist_ok=True)

# Sample signals
signals = pd.DataFrame({
    "timestamp": ["2024-06-01 09:30:00", "2024-06-02 09:30:00", "2024-06-03 09:30:00"],
    "asset": ["AAPL", "AAPL", "AAPL"],
    "signal": [1, 0, -1]
})
signals.to_csv("data/historical_signals.csv", index=False)

# Sample prices
prices = pd.DataFrame({
    "timestamp": ["2024-06-01 09:30:00", "2024-06-02 09:30:00", "2024-06-03 09:30:00"],
    "asset": ["AAPL", "AAPL", "AAPL"],
    "price": [185.0, 187.5, 182.0]
})
prices.to_csv("data/historical_prices.csv", index=False)

print("✅ Sample data generated.")

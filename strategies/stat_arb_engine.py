import pandas as pd
from datetime import datetime
from models.stat_arb_selector import (
    get_price_data,
    find_cointegrated_pairs,
    calculate_spread_zscore
)

def generate_stat_arb_signals():
    tickers = ["MSFT", "AAPL", "GOOG", "META", "AMZN"]  # Expand as needed
    prices = get_price_data(tickers)
    pairs = find_cointegrated_pairs(prices)

    signals = []

    for t1, t2, pval in pairs:
        z, spread = calculate_spread_zscore(prices[t1], prices[t2])
        latest_z = z[-1]  # ✅ FIXED: z is a NumPy array

        if abs(latest_z) > 2:
            signal = {
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "strategy": "stat_arb",
                "pair": f"{t1}-{t2}",
                "zscore": round(latest_z, 2),
                "signal": "long t1 / short t2" if latest_z < 0 else "short t1 / long t2",
                "confidence": min(abs(latest_z) / 4, 1.0),
                "t1": t1,
                "t2": t2,
                "spread": float(spread[-1])  # ✅ Convert to float for logging
            }
            signals.append(signal)

    return pd.DataFrame(signals)
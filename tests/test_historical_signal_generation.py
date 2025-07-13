from strategies.trend_following import TrendFollowingStrategy
from data.historical_data_loader import get_data

def test_signals():
    df = get_data("AAPL", "6mo", "1d")
    strategy = TrendFollowingStrategy("Trend", {"base": 1})
    
    for _, row in df.iterrows():
        data = {
            "price": row["Close"],
            "ma": row["ma"],
            "upper_band": row["upper_band"],
            "lower_band": row["lower_band"],
            "recent_high": row["recent_high"],
            "recent_low": row["recent_low"]
        }
        signal = strategy.generate_signal(data)
        print(f"{row.name} | Price: {row['Close']:.2f} | Signal: {signal}")

if __name__ == "__main__":
    test_signals()
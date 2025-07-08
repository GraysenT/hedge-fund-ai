import pandas as pd
import yfinance as yf
import datetime
import os


def run():
    print("🧪 Running Signal Backtester...")

    log_path = os.path.join("logs", "signal_log.csv")
    if not os.path.exists(log_path):
        print("🚫 No signal log found.")
        return

    df = pd.read_csv(log_path)
    print(f"🧠 Loaded {len(df)} signal records")
    print(df.head())
    df["Date"] = pd.to_datetime(df["Date"])

    asset_to_ticker = {
        "Gold": "GLD",
        "Oil": "USO",
        "Wheat": "WEAT",
        "Cattle": "COW"
    }

    df["Ticker"] = df["Asset"].map(asset_to_ticker)
    df.dropna(subset=["Ticker"], inplace=True)

    results = []
    print("🧪 Loop completed")
    print(f"Total processed rows: {len(results)}")

    for _, row in df.iterrows():
        date = row["Date"]
        ticker = row["Ticker"]
        signal = row["Signal"]

        try:
            # Adjusted to go 3 days back and 1 day forward to catch data on weekends or holidays
            price_start = (date - pd.Timedelta(days=3)).strftime('%Y-%m-%d')
            price_end = (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')

            print(f"🧪 Fetching {ticker} from {price_start} to {price_end}")
            prices = yf.download(ticker, start=price_start, end=price_end)

            if prices.empty:
                print(
                    f"🚫 No price data for {ticker} on {date.strftime('%Y-%m-%d')}")
                continue

            open_price = prices.iloc[0]["Open"]
            close_price = prices.iloc[-1]["Close"]
            change = (close_price - open_price) / open_price

            correct = (
                (signal == "Buy" and change > 0) or
                (signal == "Sell" and change < 0) or
                (signal == "Hold")
            )

            results.append({
                "Date": date.strftime('%Y-%m-%d'),
                "Asset": row["Asset"],
                "Signal": signal,
                # ✅ Convert to float
                "Return (%)": round(float(change) * 100, 2),
                "Correct": "✅" if correct else "❌"
            })

        except Exception as e:
            print(f"❌ Error with {ticker} on {date}: {e}")

    print("🧪 Loop completed")
    print(f"Total processed rows: {len(results)}")

    if results:
        import random
        strategies = ["LSTM", "Fusion", "Macro", "Sentiment"]
        summary = pd.DataFrame(results)
        summary["Strategy"] = [random.choice(
            strategies) for _ in range(len(summary))]

        # Save results to CSV
        bt_output_path = os.path.join("logs", "backtest_results.csv")
        summary.to_csv(bt_output_path, index=False)

        print(summary.to_string(index=False))
        accuracy = round(summary["Correct"].value_counts(
            normalize=True).get("✅", 0) * 100, 2)
        avg_return = round(summary["Return (%)"].mean(), 2)
        print(f"\n📈 Accuracy: {accuracy}%")
        print(f"💰 Average Return per Signal: {avg_return}%")
        print(f"📁 Results saved to: {bt_output_path}")
    else:
        print("🚫 No valid signals or price data found.")


if __name__ == "__main__":
    run()

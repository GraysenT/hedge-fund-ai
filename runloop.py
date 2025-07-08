import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from data.quote_feed import get_latest_price
from data.crypto_feed import get_crypto_price
from execution.execution_router import route_order
from execution.alpaca_router import place_alpaca_order
from alerts.slack_notifier import send_slack_alert

load_dotenv()

TICKERS = ["AAPL", "TSLA", "SPY", "BTC", "ETH"]
TRADE_LOG = "logs/trade_history.json"
SIGNAL_LOG = "logs/signal_events.json"

USE_ALPACA = True  # ✅ Toggle for Alpaca live trades
USE_CRYPTO = True  # ✅ Crypto support (CoinGecko)

def fetch_price(ticker):
    if ticker.upper() in ["BTC", "ETH"] and USE_CRYPTO:
        price = get_crypto_price(ticker.lower())
        return {"ticker": ticker, "last": price, "source": "CoinGecko"} if price else None
    return get_latest_price(ticker)

def generate_signal(price, threshold=150):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "asset": price["ticker"],
        "source": price.get("source", "Polygon"),
        "price": price["last"],
        "action": "BUY" if price["last"] > threshold else "HOLD",
        "confidence": 0.9
    }

def run_main_cycle():
    print(f"\n🧠 Starting Hedge Fund AI Main Loop...")
    os.makedirs("logs", exist_ok=True)

    try:
        with open(TRADE_LOG, "r") as f:
            existing_trades = json.load(f)
    except:
        existing_trades = []

    new_signals = []
    new_trades = []

    for ticker in TICKERS:
        price = fetch_price(ticker)
        if not price:
            continue

        signal = generate_signal(price)
        new_signals.append(signal)
        print(f"📡 Signal: {signal}")

        if signal["action"] == "BUY":
            if USE_ALPACA and ticker.upper() not in ["BTC", "ETH"]:
                alpaca_order = place_alpaca_order(signal["asset"], qty=1, side="buy")
                execution_note = "Alpaca executed" if alpaca_order else "Alpaca failed"
            else:
                execution = route_order({
                    "asset": signal["asset"],
                    "size": 100,
                    "volatility": 0.02,
                    "liquidity": "high"
                })
                execution_note = "Simulated"
                trade = {
                    "timestamp": signal["timestamp"],
                    "strategy": "live_signal",
                    "asset": signal["asset"],
                    "action": "BUY",
                    "size": 100,
                    "price": signal["price"],
                    "pnl": round(-1 * execution["expected_slippage"], 2),
                    "method": execution["method"],
                    "venue": execution["venue"]
                }
                new_trades.append(trade)
                print(f"💰 Trade Executed: {trade}")

            send_slack_alert(f"🟢 {signal['asset']} → {signal['action']} @ {signal['price']} ({execution_note})", tag="TRADE")

    with open(SIGNAL_LOG, "w") as f:
        json.dump(new_signals, f, indent=2)

    with open(TRADE_LOG, "w") as f:
        json.dump(existing_trades + new_trades, f, indent=2)

    print("✅ Runloop complete.")

if __name__ == "__main__":
    while True:
        run_main_cycle()
        time.sleep(60)  # ⏱ every 60 seconds
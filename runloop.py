import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv

from data.quote_feed import get_latest_price
from strategies.stat_arb_engine import generate_stat_arb_signal
from strategies.macro_sentiment import generate_macro_sentiment_signal
from strategies.crypto_edge import generate_crypto_signal
from execution.execution_router import route_order
from execution.alpaca_router import place_alpaca_order
from alerts.slack_notifier import send_slack_alert

load_dotenv()

TICKERS = ["AAPL", "TSLA", "SPY", "BTC/USD", "ETH/USD"]
TRADE_LOG = "logs/trade_history.json"
SIGNAL_LOG = "logs/signal_events.json"

USE_ALPACA = True
USE_CRYPTO = True

def fetch_signal(ticker, price):
    if ticker in ["AAPL", "TSLA"]:
        return generate_stat_arb_signal(ticker, price)
    elif ticker == "SPY":
        return generate_macro_sentiment_signal(ticker, price)
    elif ticker in ["BTC/USD", "ETH/USD"]:
        return generate_crypto_signal(ticker, price)
    else:
        return None

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
        price_data = get_latest_price(ticker)
        if not price_data or not price_data.get("last"):
            continue

        signal = fetch_signal(ticker, price_data["last"])
        if not signal:
            continue

        signal["timestamp"] = datetime.utcnow().isoformat()
        new_signals.append(signal)
        print(f"📡 Signal: {signal}")

        if signal["action"] == "BUY":
            if USE_ALPACA and ticker not in ["BTC/USD", "ETH/USD"]:
                place_alpaca_order(signal["asset"], qty=1, side="buy")
                execution_note = "Alpaca executed"
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
                    "strategy": signal["strategy"],
                    "asset": signal["asset"],
                    "action": signal["action"],
                    "size": 100,
                    "price": signal["price"],
                    "pnl": round(-1 * execution["expected_slippage"], 2),
                    "method": execution["method"],
                    "venue": execution["venue"]
                }
                new_trades.append(trade)
                print(f"💰 Trade Executed: {trade}")

            send_slack_alert(
                f"🟢 {signal['asset']} → {signal['action']} @ {signal['price']} ({execution_note})",
                tag="TRADE"
            )

    with open(SIGNAL_LOG, "w") as f:
        json.dump(new_signals, f, indent=2)

    with open(TRADE_LOG, "w") as f:
        json.dump(existing_trades + new_trades, f, indent=2)

    print("✅ Runloop complete.")

if __name__ == "__main__":
    while True:
        run_main_cycle()
        time.sleep(60)  # Run every 60 seconds
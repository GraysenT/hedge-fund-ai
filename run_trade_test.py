from execution.trade_runner import TradeRunner

runner = TradeRunner(
    strategy_region_map={"US_Trend": "US", "Crypto_RSI": "Crypto"},
    strategy_ticker_map={"US_Trend": "SPY", "Crypto_RSI": "BTCUSD"},
    account_equity=100000
)

# Simulated current positions and targets
current_positions = {"US_Trend": 0.20, "Crypto_RSI": 0.60}
target_weights = {"US_Trend": 0.30, "Crypto_RSI": 0.50}
latest_prices = {"SPY": 440.0, "BTCUSD": 61000}

trades = runner.run(current_positions, target_weights, latest_prices)

print("Trades executed and logged to trade_logs.csv:")
for trade in trades:
    print(trade)

import csv
import time

class TradeOutcomeTracer:
    def __init__(self, filename="trade_outcomes.csv"):
        self.filename = filename
        with open(self.filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "symbol", "action", "entry_price", "exit_price", "return"])

    def log_trade(self, symbol, action, entry_price, exit_price):
        trade_return = round((exit_price - entry_price) / entry_price, 4)
        if action == "SELL":
            trade_return *= -1
        with open(self.filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime('%Y-%m-%d %H:%M:%S'),
                symbol,
                action,
                entry_price,
                exit_price,
                trade_return
            ])
        print(f"[TRADE LOGGED] {symbol} {action} → Return: {trade_return * 100:.2f}%")
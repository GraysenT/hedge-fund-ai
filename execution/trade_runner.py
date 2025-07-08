import os
import csv
from datetime import datetime
from execution.trade_executor import TradeExecutor
from execution.strategy_mapper import StrategyTradeMapper
from brokers.alpaca_executor import AlpacaExecutor

class TradeRunner:
    def __init__(self, strategy_region_map, strategy_ticker_map, account_equity=100000):
        self.trade_executor = TradeExecutor(execution_threshold=0.05)
        self.mapper = StrategyTradeMapper(strategy_ticker_map, account_equity)
        self.broker = AlpacaExecutor()
        self.strategy_region_map = strategy_region_map
        self.log_file = "trade_logs.csv"

        # Ensure log file has headers
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", "strategy", "ticker", "side", "qty",
                    "price", "dollars", "tag", "status"
                ])

    def run(self, current_positions, target_weights, latest_prices):
        orders = self.trade_executor.generate_orders(current_positions, target_weights)
        trades = self.mapper.generate_trade_details(orders, latest_prices)

        for trade in trades:
            response = self.broker.place_order(trade["ticker"], trade["qty"], trade["side"])
            status = response["status"]

            # Log enriched trade with strategy
            with open(self.log_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().isoformat(),
                    trade["strategy"],  # ✅ Include strategy here
                    trade["ticker"],
                    trade["side"],
                    trade["qty"],
                    trade["price"],
                    trade["allocated_dollars"],
                    trade["tag"],
                    status
                ])

        return trades
    
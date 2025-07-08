import time
from typing import Dict

class TradeExecutor:
    def __init__(self, mode='paper'):
        self.mode = mode  # 'live' or 'paper'
        self.executed_orders = []

    def execute_trade(self, signal: Dict):
        order = {
            "symbol": signal["symbol"],
            "action": signal["action"],
            "confidence": signal["confidence"],
            "timestamp": time.time(),
            "mode": self.mode
        }

        if self.mode == 'live':
            self._send_to_broker(order)
        else:
            self._log_paper_trade(order)

        self.executed_orders.append(order)
        return order

    def _send_to_broker(self, order: Dict):
        print(f"[LIVE EXECUTION] Sending order to broker: {order}")
        # Integration with real broker API (e.g., Alpaca/IBKR) goes here

    def _log_paper_trade(self, order: Dict):
        print(f"[PAPER EXECUTION] Simulated trade: {order}")
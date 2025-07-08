class StrategyTradeMapper:
    def __init__(self, strategy_ticker_map, account_equity=100000, min_trade_size=1000):
        """
        Args:
            strategy_ticker_map (dict): strategy name → ticker
            account_equity (float): total equity available for allocation
            min_trade_size (float): minimum dollar amount per trade
        """
        self.strategy_ticker_map = strategy_ticker_map
        self.account_equity = account_equity
        self.min_trade_size = min_trade_size

    def generate_trade_details(self, orders, latest_prices):
        """
        Args:
            orders (list of dicts): each with 'strategy', 'action', 'delta_weight'
            latest_prices (dict): ticker → latest price
        Returns:
            list of dicts: each with ticker, qty, side, and strategy metadata
        """
        trades = []

        for order in orders:
            strat = order["strategy"]
            ticker = self.strategy_ticker_map.get(strat)
            delta_weight = abs(order["delta_weight"])
            dollar_alloc = self.account_equity * delta_weight

            if not ticker or dollar_alloc < self.min_trade_size:
                continue  # skip if unknown ticker or trade too small

            price = latest_prices.get(ticker)
            if not price or price <= 0:
                continue  # skip if no price

            qty = int(dollar_alloc // price)
            if qty == 0:
                continue  # skip if not enough size

            trades.append({
                "strategy": strat,
                "ticker": ticker,
                "qty": qty,
                "side": order["action"],
                "allocated_dollars": round(dollar_alloc, 2),
                "price": round(price, 2),
                "tag": f"{strat}-{order['action']}"
            })

        return trades

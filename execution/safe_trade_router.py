class SafeTradeRouter:
    def __init__(self, executor, max_loss=0.05, max_trade_size=1000):
        self.executor = executor
        self.max_loss = max_loss
        self.max_trade_size = max_trade_size
        self.pnl_history = []

    def safe_execute(self, symbol, action, size, price, account_balance):
        # Sanity checks
        if size * price > self.max_trade_size:
            print(f"⚠️ Trade too large — BLOCKED")
            return
        projected_loss = size * price * 0.02  # assume 2% slip
        if projected_loss > self.max_loss * account_balance:
            print(f"⚠️ Risk breach — BLOCKED")
            return
        self.executor.place_order(symbol, action, size)
        print(f"✅ Executed {action} {size} {symbol} at {price}")
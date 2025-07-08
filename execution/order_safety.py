class OrderSafety:
    def __init__(self, max_trade_size=100000, max_slippage=0.02):
        self.max_trade_size = max_trade_size
        self.max_slippage = max_slippage

    def is_safe(self, signal, estimated_slippage=0.01):
        trade_size = signal.get("confidence", 0) * 100000
        if trade_size > self.max_trade_size:
            print(f"[SAFETY] Trade size too large: ${trade_size:.2f}")
            return False

        if estimated_slippage > self.max_slippage:
            print(f"[SAFETY] Slippage too high: {estimated_slippage:.2f}")
            return False

        return True
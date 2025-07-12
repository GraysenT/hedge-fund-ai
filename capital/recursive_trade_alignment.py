class RecursiveTradeAlignment:
    def __init__(self):
        self.aligned_trades = []

    def align_trade_with_purpose(self, trade_id, purpose):
        """Align trades with the system’s recursive purpose."""
        aligned_trade = {"trade_id": trade_id, "purpose": purpose}
        self.aligned_trades.append(aligned_trade)
        print(f"Aligned trade {trade_id} with purpose: {purpose}")
    
    def get_aligned_trades(self):
        return self.aligned_trades
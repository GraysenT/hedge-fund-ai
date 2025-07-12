class RecursiveTradePurposeAligner:
    def __init__(self):
        self.aligned_trades = []

    def align_trade_with_purpose(self, trade_id, purpose):
        """Align individual trades with the system’s recursive purpose."""
        trade_alignment = {"trade_id": trade_id, "purpose": purpose}
        self.aligned_trades.append(trade_alignment)
        print(f"Aligned trade {trade_id} with purpose: {purpose}")
    
    def get_aligned_trades(self):
        return self.aligned_trades
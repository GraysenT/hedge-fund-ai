class RiskManager:
    def __init__(self, max_risk=0.02):
        self.max_risk = max_risk  # Max risk per trade (2%)

    def calculate_position_size(self, live_data):
        """Calculate position size based on account balance and risk."""
        account_balance = 100000  # Example balance
        trade_risk = live_data["AAPL"][-1] * 0.02  # 2% risk on trade
        position_size = account_balance * self.max_risk / trade_risk
        return position_size

    def place_trade(self, strategy, position_size):
        """Place the trade (buy/sell) based on the strategy signal."""
        if strategy == "buy":
            print(f"Placing buy order with size {position_size}")
        elif strategy == "sell":
            print(f"Placing sell order with size {position_size}")
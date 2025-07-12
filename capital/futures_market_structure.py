class FuturesMarketStructure:
    def __init__(self):
        self.market_conditions = {}

    def track_market_structure(self, contract_symbol, condition):
        """Track market conditions for a given futures contract (e.g., backwardation, contango)."""
        self.market_conditions[contract_symbol] = condition
        print(f"Market condition for {contract_symbol} tracked as: {condition}")
    
    def get_market_conditions(self):
        return self.market_conditions

    def calculate_rollover(self, contract_symbol, expiration_date, current_date):
        """Calculate whether a rollover is necessary based on contract expiration and current date."""
        if current_date >= expiration_date:
            print(f"Rollover required for {contract_symbol}!")
            # Logic for handling the rollover (e.g., moving to the next contract)
            return True
        return False
    
    def is_backwardation(self, front_month_price, back_month_price):
        """Check if the market is in backwardation (front-month contract is more expensive)."""
        return front_month_price > back_month_price
    
    def is_contango(self, front_month_price, back_month_price):
        """Check if the market is in contango (front-month contract is cheaper)."""
        return front_month_price < back_month_price
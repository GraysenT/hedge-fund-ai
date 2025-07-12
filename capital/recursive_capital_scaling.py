class RecursiveCapitalScaling:
    def __init__(self):
        self.scaled_capital = []

    def scale_capital_over_time(self, capital_amount, scaling_factor):
        """Scale capital recursively to ensure long-term optimization."""
        scaled_amount = capital_amount * scaling_factor
        self.scaled_capital.append(scaled_amount)
        print(f"Scaled capital: {scaled_amount} with scaling factor: {scaling_factor}")
    
    def get_scaled_capital(self):
        return self.scaled_capital
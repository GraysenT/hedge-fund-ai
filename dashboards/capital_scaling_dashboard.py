class CapitalScalingDashboard:
    def __init__(self):
        self.scaled_capital = []

    def track_scaled_capital(self, capital_amount, scaling_factor):
        """Track capital scaling across recursive logic."""
        self.scaled_capital.append({"capital_amount": capital_amount, "scaling_factor": scaling_factor})
        print(f"Tracked scaled capital: {capital_amount} with factor: {scaling_factor}")
    
    def visualize_capital_scaling(self):
        """Visualize capital scaling process across the system."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Capital Scaling")
        capital_amounts = [entry["capital_amount"] for entry in self.scaled_capital]
        scaling_factors = [entry["scaling_factor"] for entry in self.scaled_capital]
        plt.plot(capital_amounts, scaling_factors, label='Capital Scaling')
        plt.xlabel("Capital Amount")
        plt.ylabel("Scaling Factor")
        plt.legend()
        plt.show()
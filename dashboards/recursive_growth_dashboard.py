class RecursiveGrowthDashboard:
    def __init__(self):
        self.growth_data = []

    def track_growth(self, amount, purpose):
        """Track and display capital growth over time."""
        self.growth_data.append({"amount": amount, "purpose": purpose})
        print(f"Tracked growth: {amount} for purpose: {purpose}")
    
    def visualize_growth(self):
        """Visualize recursive capital growth."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Recursive Capital Growth")
        amounts = [entry["amount"] for entry in self.growth_data]
        purposes = [entry["purpose"] for entry in self.growth_data]
        plt.plot(amounts, label='Growth Amount')
        plt.xlabel("Time")
        plt.ylabel("Amount")
        plt.legend()
        plt.show()
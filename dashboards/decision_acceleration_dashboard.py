class DecisionAccelerationDashboard:
    def __init__(self):
        self.decisions = []

    def track_decision(self, decision_name, factor):
        """Track the acceleration of decisions across recursive logic."""
        self.decisions.append({"decision_name": decision_name, "factor": factor})
        print(f"Tracked decision: {decision_name} with factor: {factor}")
    
    def visualize_decisions(self):
        """Visualize decision acceleration in real time."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Decision Acceleration")
        decision_names = [entry["decision_name"] for entry in self.decisions]
        factors = [entry["factor"] for entry in self.decisions]
        plt.bar(decision_names, factors)
        plt.xlabel("Decision")
        plt.ylabel("Acceleration Factor")
        plt.show()
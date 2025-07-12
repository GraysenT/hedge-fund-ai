class PurposeFulfillmentDashboard:
    def __init__(self):
        self.fulfillment_log = []

    def track_fulfillment(self, purpose, progress):
        """Monitor the fulfillment of recursive purpose."""
        self.fulfillment_log.append({"purpose": purpose, "progress": progress})
        print(f"Tracked fulfillment: {purpose} with progress: {progress}%")
    
    def visualize_fulfillment(self):
        """Visualize purpose fulfillment progress."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Purpose Fulfillment Progress")
        purposes = [entry["purpose"] for entry in self.fulfillment_log]
        progress = [entry["progress"] for entry in self.fulfillment_log]
        plt.bar(purposes, progress)
        plt.xlabel("Purpose")
        plt.ylabel("Progress (%)")
        plt.show()
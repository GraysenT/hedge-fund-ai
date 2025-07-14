class CrossDimensionalDashboard:
    def __init__(self):
        self.allocations = []

    def track_allocation(self, dimension, resource_name, allocation_amount):
        """Track resource allocation across multiple dimensions."""
        self.allocations.append({"dimension": dimension, "resource_name": resource_name, "allocation_amount": allocation_amount})
        print(f"Tracked allocation of {resource_name} in dimension {dimension} with amount: {allocation_amount}")
    
    def visualize_allocations(self):
        """Visualize resource allocations across dimensions."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Cross-Dimensional Resource Allocation")
        dimensions = [entry["dimension"] for entry in self.allocations]
        allocation_amounts = [entry["allocation_amount"] for entry in self.allocations]
        plt.bar(dimensions, allocation_amounts)
        plt.xlabel("Dimension")
        plt.ylabel("Allocation Amount")
        plt.show()
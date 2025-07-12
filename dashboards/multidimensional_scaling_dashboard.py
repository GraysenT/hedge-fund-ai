class MultidimensionalScalingDashboard:
    def __init__(self):
        self.scaling_data = []

    def track_scaling(self, dimension_name, scaling_factor):
        """Track recursive scaling across multiple dimensions."""
        self.scaling_data.append({"dimension_name": dimension_name, "scaling_factor": scaling_factor})
        print(f"Tracked scaling of dimension: {dimension_name} with factor: {scaling_factor}")
    
    def visualize_scaling(self):
        """Visualize the scaling process across multiple dimensions."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Multidimensional Scaling")
        dimensions = [entry["dimension_name"] for entry in self.scaling_data]
        scaling_factors = [entry["scaling_factor"] for entry in self.scaling_data]
        plt.plot(dimensions, scaling_factors, label="Scaling Factor")
        plt.xlabel("Dimension")
        plt.ylabel("Scaling Factor")
        plt.legend()
        plt.show()
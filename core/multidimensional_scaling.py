class MultidimensionalScaling:
    def __init__(self):
        self.dimensions = []

    def scale_dimension(self, dimension_name, scaling_factor):
        """Scale across multiple dimensions of recursive evolution."""
        dimension = {"dimension_name": dimension_name, "scaling_factor": scaling_factor}
        self.dimensions.append(dimension)
        print(f"Scaled dimension: {dimension_name} with factor: {scaling_factor}")
    
    def get_scaled_dimensions(self):
        return self.dimensions
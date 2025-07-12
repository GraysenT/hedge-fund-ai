class SelfOptimization:
    def __init__(self):
        self.optimization_level = "Initial Optimization"

    def optimize_system(self, level):
        """Optimize the system recursively for better performance."""
        self.optimization_level = level
        print(f"Optimized system to: {self.optimization_level}")
    
    def get_optimization_level(self):
        return self.optimization_level
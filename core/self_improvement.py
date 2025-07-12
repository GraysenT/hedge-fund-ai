class SelfImprovement:
    def __init__(self):
        self.improvement_level = "Initial Improvement"

    def improve_system(self, improvement_factor):
        """Apply recursive self-improvement mechanisms to the system."""
        self.improvement_level = improvement_factor
        print(f"System improved to: {self.improvement_level}")
    
    def get_improvement_level(self):
        return self.improvement_level
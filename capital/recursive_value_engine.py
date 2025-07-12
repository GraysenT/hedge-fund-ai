class RecursiveValueEngine:
    def __init__(self):
        self.values = []

    def assign_value(self, value_name, value):
        """Assign values to recursive capital logic."""
        value_assignment = {"name": value_name, "value": value}
        self.values.append(value_assignment)
        print(f"Assigned value: {value_name} = {value}")
    
    def get_values(self):
        return self.values
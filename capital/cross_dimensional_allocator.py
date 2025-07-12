class CrossDimensionalAllocator:
    def __init__(self):
        self.allocations = []

    def allocate_resources_across_dimensions(self, dimension, resource_name, allocation_amount):
        """Allocate resources across multiple dimensions of recursive logic."""
        allocation = {"dimension": dimension, "resource_name": resource_name, "allocation_amount": allocation_amount}
        self.allocations.append(allocation)
        print(f"Allocated {allocation_amount} of {resource_name} to dimension: {dimension}")
    
    def get_allocations(self):
        return self.allocations
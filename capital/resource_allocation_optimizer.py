class ResourceAllocationOptimizer:
    def __init__(self):
        self.optimized_allocations = []

    def optimize_allocation(self, resource_name, allocation_factor):
        """Optimize resource allocation for better recursive impact across dimensions."""
        optimized_allocation = {"resource_name": resource_name, "allocation_factor": allocation_factor}
        self.optimized_allocations.append(optimized_allocation)
        print(f"Optimized allocation for {resource_name} with factor: {allocation_factor}")
    
    def get_optimized_allocations(self):
        return self.optimized_allocations
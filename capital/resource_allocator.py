class ResourceAllocator:
    def __init__(self):
        self.allocations = []

    def allocate_resources(self, resource_name, allocation_amount):
        """Allocate resources based on recursive scaling and strategy requirements."""
        allocation = {"resource_name": resource_name, "allocation_amount": allocation_amount}
        self.allocations.append(allocation)
        print(f"Allocated resource {resource_name} with amount: {allocation_amount}")
    
    def get_allocations(self):
        return self.allocations
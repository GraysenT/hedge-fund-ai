class CrossRealityResourceAllocator:
    def __init__(self):
        self.resources = []

    def allocate_resources_across_reality(self, reality_name, resource_name, amount):
        """Allocate resources across different realities and domains."""
        allocation = {"reality_name": reality_name, "resource_name": resource_name, "amount": amount}
        self.resources.append(allocation)
        print(f"Allocated {amount} of {resource_name} to reality: {reality_name}")
    
    def get_allocated_resources(self):
        return self.resources
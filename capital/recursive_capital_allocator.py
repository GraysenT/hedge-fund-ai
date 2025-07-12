class RecursiveCapitalAllocator:
    def __init__(self):
        self.allocations = []

    def allocate_capital(self, amount, purpose):
        """Allocate capital based on recursive evolution and purpose."""
        allocation = {"amount": amount, "purpose": purpose}
        self.allocations.append(allocation)
        print(f"Allocated {amount} to purpose: {purpose}")
    
    def get_allocations(self):
        return self.allocations
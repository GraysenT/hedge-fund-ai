class QuantumCapitalAllocator:
    def __init__(self):
        self.allocations = []

    def allocate_capital_quantum(self, amount, quantum_factor):
        """Allocate capital using quantum strategies to maximize recursive evolution."""
        allocation = {"amount": amount, "quantum_factor": quantum_factor}
        self.allocations.append(allocation)
        print(f"Allocated {amount} capital with quantum factor: {quantum_factor}")
    
    def get_allocations(self):
        return self.allocations
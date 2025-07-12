class QuantumStateEvolution:
    def __init__(self):
        self.quantum_states = []

    def evolve_to_quantum_state(self, state_name, quantum_factor):
        """Evolve the system to a new quantum state."""
        state = {"state_name": state_name, "quantum_factor": quantum_factor}
        self.quantum_states.append(state)
        print(f"Evolved to quantum state: {state_name} with factor: {quantum_factor}")
    
    def get_quantum_states(self):
        return self.quantum_states
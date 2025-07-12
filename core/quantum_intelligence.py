class QuantumIntelligence:
    def __init__(self):
        self.quantum_states = []

    def transition_to_quantum_state(self, state):
        """Transition the system to a new quantum state."""
        self.quantum_states.append(state)
        print(f"System transitioned to quantum state: {state}")
    
    def get_quantum_states(self):
        return self.quantum_states
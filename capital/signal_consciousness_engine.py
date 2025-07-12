class SignalConsciousnessEngine:
    def __init__(self):
        self.signals = []

    def evolve_signal(self, signal):
        """Evolves signals with memory, belief, and meaning."""
        evolved_signal = signal + "_evolved"
        self.signals.append(evolved_signal)
        print(f"Evolved signal: {evolved_signal}")
    
    def get_signals(self):
        return self.signals
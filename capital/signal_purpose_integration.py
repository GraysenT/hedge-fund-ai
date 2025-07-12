class SignalPurposeIntegration:
    def __init__(self):
        self.integrated_signals = []

    def integrate_signal_with_purpose(self, signal, purpose):
        """Integrates signals with recursive capital purpose."""
        integrated_signal = {"signal": signal, "purpose": purpose}
        self.integrated_signals.append(integrated_signal)
        print(f"Integrated signal: {signal} with purpose: {purpose}")
    
    def get_integrated_signals(self):
        return self.integrated_signals
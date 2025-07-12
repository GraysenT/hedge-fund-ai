class DecisionMaking:
    def __init__(self):
        self.decisions = []

    def make_decision(self, situation, decision_factor):
        """Make autonomous decisions based on the system's recursive feedback."""
        decision = {"situation": situation, "decision_factor": decision_factor}
        self.decisions.append(decision)
        print(f"Made decision for {situation} with factor: {decision_factor}")
    
    def get_decisions(self):
        return self.decisions
class AdaptiveDecisionMaker:
    def __init__(self):
        self.decisions = []

    def make_decision(self, situation, decision_factor):
        """Make a recursive decision based on the situation and decision factor."""
        decision = {"situation": situation, "decision_factor": decision_factor, "status": "made"}
        self.decisions.append(decision)
        print(f"Made decision for {situation} with factor: {decision_factor}")
    
    def get_decisions(self):
        return self.decisions
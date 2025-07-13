from datetime import datetime

class ContextBelief:
    def __init__(self, context_name, belief_statement, belief_strength=0.5):
        self.context = context_name            # e.g., "Recession", "AI Regime", "Fed Easing"
        self.statement = belief_statement      # natural language or symbolic
        self.strength = belief_strength        # 0.0 to 1.0
        self.history = [{
            "timestamp": datetime.now().isoformat(),
            "value": belief_strength
        }]

    def update_belief(self, new_strength):
        self.strength = new_strength
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "value": new_strength
        })

    def serialize(self):
        return {
            "context": self.context,
            "statement": self.statement,
            "current_strength": self.strength,
            "history": self.history
        }
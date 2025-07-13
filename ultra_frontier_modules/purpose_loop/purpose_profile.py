import uuid
from datetime import datetime

class PurposeProfile:
    def __init__(self, name, core_directive, intent_score=0.5):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created = datetime.now().isoformat()
        self.core_directive = core_directive
        self.intent_score = intent_score
        self.history = []

    def reflect_on_action(self, action_summary, outcome_score):
        reflection = {
            "timestamp": datetime.now().isoformat(),
            "action": action_summary,
            "outcome_score": outcome_score,
            "alignment": self.compute_alignment(outcome_score)
        }
        self.history.append(reflection)
        return reflection

    def compute_alignment(self, outcome_score):
        deviation = abs(outcome_score - self.intent_score)
        return round(1 - deviation, 3)

    def evolve_purpose(self):
        if not self.history:
            return self.core_directive
        alignment_avg = sum(h["alignment"] for h in self.history[-5:]) / len(self.history[-5:])
        if alignment_avg < 0.6:
            self.intent_score += 0.05
            self.core_directive = "Refine strategy clarity"
        elif alignment_avg > 0.85:
            self.core_directive = "Expand capital influence"
        return self.core_directive
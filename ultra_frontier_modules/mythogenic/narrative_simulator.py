import random

class MythicNarrative:
    def __init__(self, theme, trust_score=0.5):
        self.theme = theme
        self.trust_score = trust_score
        self.perceived_strength = 0.5

    def simulate_reinforcement(self, media_boost=0.1, outcome_alignment=0.2):
        delta = media_boost + outcome_alignment
        self.trust_score = min(1.0, self.trust_score + delta)
        self.perceived_strength += delta * 0.5

    def simulate_collapse(self, exposure=0.3, contradiction=0.2):
        collapse = exposure * contradiction
        self.trust_score = max(0.0, self.trust_score - collapse)
        self.perceived_strength -= collapse * 0.4

    def summary(self):
        return {
            "Theme": self.theme,
            "Trust": round(self.trust_score, 3),
            "Strength": round(self.perceived_strength, 3)
        }
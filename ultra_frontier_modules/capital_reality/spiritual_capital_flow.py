import random

class SpiritualMarketAgent:
    def __init__(self, name, belief_bias, ritual_alignment, emotional_volatility):
        self.name = name
        self.bias = belief_bias  # 0–1
        self.alignment = ritual_alignment  # 0–1
        self.volatility = emotional_volatility  # 0–1
        self.trust_in_market = 0.5

    def update(self, collective_signal, narrative_shift):
        mood_swing = collective_signal * self.bias + narrative_shift * self.alignment
        self.trust_in_market += mood_swing * (1 - self.volatility)
        self.trust_in_market = min(max(self.trust_in_market, 0), 1)

    def express(self):
        if self.trust_in_market > 0.7:
            return "Invest Spiritually"
        elif self.trust_in_market < 0.3:
            return "Withdraw Faith"
        else:
            return "Observe in Stillness"
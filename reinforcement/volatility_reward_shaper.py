class VolatilityRewardShaper:
    def __init__(self):
        self.history = []

    def adjust(self, base_reward, volatility):
        multiplier = 1.0
        if volatility > 0.4:
            multiplier = 0.8  # downweight due to risk
        elif volatility < 0.15:
            multiplier = 1.1  # boost for stable environment

        shaped = round(base_reward * multiplier, 4)
        print(f"[VOL REWARD] Base: {base_reward:.3f}, Vol: {volatility:.3f} → Shaped: {shaped:.3f}")
        return shaped
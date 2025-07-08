class ReinforcementThrottle:
    def __init__(self, decay_threshold=0.2, reward_floor=0.5):
        self.decay_threshold = decay_threshold
        self.reward_floor = reward_floor

    def should_promote(self, score):
        return score >= self.reward_floor

    def should_mute(self, score):
        return score <= self.decay_threshold

    def assess(self, strategy_name, score):
        if self.should_promote(score):
            print(f"[REINFORCEMENT] {strategy_name} is being promoted")
        elif self.should_mute(score):
            print(f"[REINFORCEMENT] {strategy_name} is being muted")
        else:
            print(f"[REINFORCEMENT] {strategy_name} is neutral")
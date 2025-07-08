class AlphaDecayGuard:
    def __init__(self, decay_threshold=0.15):
        self.threshold = decay_threshold

    def check_decay(self, current_score, historical_score):
        decay = (historical_score - current_score) / historical_score if historical_score else 0
        if decay > self.threshold:
            print(f"[ALPHA DECAY] Score dropped {decay:.2%}. Strategy should be reviewed.")
            return True
        return False
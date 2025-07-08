class WeightOverlay:
    def __init__(self):
        self.weights = {}

    def apply_weight(self, signal):
        strategy = signal.get("strategy")
        weight = self.weights.get(strategy, 1.0)
        signal["weighted_confidence"] = round(signal["confidence"] * weight, 3)
        return signal

    def update_weight(self, strategy, new_weight):
        self.weights[strategy] = new_weight
        print(f"[WEIGHT UPDATED] {strategy}: {new_weight}")

    def get_weights(self):
        return self.weights

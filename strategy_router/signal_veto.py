class SignalVeto:
    def __init__(self, confidence_threshold=0.6):
        self.confidence_threshold = confidence_threshold
        self.vetoed = []

    def check(self, signal):
        if signal.get("confidence", 0) < self.confidence_threshold:
            self.vetoed.append(signal)
            print(f"[VETO] Signal vetoed: {signal}")
            return True
        return False

    def get_vetoed(self):
        return self.vetoed
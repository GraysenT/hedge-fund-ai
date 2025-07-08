from collections import defaultdict

class AlphaAttribution:
    def __init__(self):
        self.impact = defaultdict(float)

    def record(self, strategy, contribution):
        self.impact[strategy] += contribution
        print(f"[ATTRIBUTION] {strategy} alpha += {contribution:.4f}")

    def report(self):
        return sorted(self.impact.items(), key=lambda x: -x[1])
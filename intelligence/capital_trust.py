class CapitalTrustScorer:
    def __init__(self):
        self.trust_scores = {}

    def update(self, strategy, pnl, volatility):
        score = max(0, pnl / (volatility + 1e-5))
        self.trust_scores[strategy] = round(score, 3)
        print(f"[TRUST] {strategy} score updated: {score:.3f}")
        return score

    def get_scores(self):
        return self.trust_scores
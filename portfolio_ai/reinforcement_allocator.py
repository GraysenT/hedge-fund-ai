from reinforcement.strategy_score import StrategyScoreTracker

class ReinforcementAllocator:
    def __init__(self, score_tracker: StrategyScoreTracker):
        self.tracker = score_tracker

    def compute_weights(self):
        scores = self.tracker.scores
        total_score = sum(max(score, 0) for score in scores.values())
        if total_score == 0:
            return {k: 1/len(scores) for k in scores}  # equal weights fallback

        return {k: max(score, 0)/total_score for k, score in scores.items()}
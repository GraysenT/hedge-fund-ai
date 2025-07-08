class WeightDecayEngine:
    def apply(self, weights: dict, performance_log):
        """
        Slightly decay weights of underperforming strategies.
        Assumes performance_log has 'strategy' and 'reward' columns.
        """
        if performance_log is None or performance_log.empty:
            return weights

        reward_by_strategy = performance_log.groupby("strategy")["reward"].mean().to_dict()
        decayed = {}
        for strat, weight in weights.items():
            decay = 1 - max(-0.5, min(reward_by_strategy.get(strat, 0), 0))  # penalize negative reward
            decayed[strat] = weight * decay

        # Normalize
        total = sum(decayed.values())
        if total > 0:
            for k in decayed:
                decayed[k] /= total
        else:
            decayed = weights

        return decayed

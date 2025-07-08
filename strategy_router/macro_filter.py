class MacroStrategyFilter:
    def __init__(self, strategy_region_map, regime_penalties=None):
        """
        Args:
            strategy_region_map: dict of strategy → region
            regime_penalties: dict of regime → penalty multiplier
        """
        self.strategy_region_map = strategy_region_map
        self.regime_penalties = regime_penalties or {
            "recession": 0.5,
            "tightening": 0.7,
            "neutral": 1.0,
            "easing": 1.2
        }

    def apply(self, base_weights, region_regimes):
        """
        Reweights strategies based on their region's macro regime.
        Args:
            base_weights: dict of strategy → weight
            region_regimes: dict of region → regime label
        Returns:
            dict of strategy → adjusted weight
        """
        adjusted = {}
        for strat, weight in base_weights.items():
            region = self.strategy_region_map.get(strat, "US")
            regime = region_regimes.get(region, "neutral")
            penalty = self.regime_penalties.get(regime, 1.0)
            adjusted[strat] = weight * penalty

        # Normalize
        total = sum(adjusted.values())
        if total > 0:
            for k in adjusted:
                adjusted[k] /= total
        return adjusted

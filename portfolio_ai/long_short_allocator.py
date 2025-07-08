class LongShortAllocator:
    def __init__(self, max_short_exposure=0.4, net_exposure_limit=1.0):
        """
        Args:
            max_short_exposure: max portion of capital allowed for shorts
            net_exposure_limit: total long - short exposure must be <= this
        """
        self.max_short = max_short_exposure
        self.net_limit = net_exposure_limit

    def allocate(self, strategy_signals, raw_weights):
        """
        Args:
            strategy_signals (dict): strategy -> 'buy' or 'sell'
            raw_weights (dict): strategy -> base allocation weight
        Returns:
            dict of strategy -> signed weight (positive for long, negative for short)
        """
        longs = {}
        shorts = {}

        for strat, signal in strategy_signals.items():
            weight = raw_weights.get(strat, 0)
            if signal == "buy":
                longs[strat] = weight
            elif signal == "sell":
                shorts[strat] = weight

        total_long = sum(longs.values())
        total_short = sum(shorts.values())

        # Normalize long and short sides separately
        if total_long > 0:
            for k in longs:
                longs[k] = longs[k] / total_long
        if total_short > 0:
            for k in shorts:
                shorts[k] = -shorts[k] / total_short * min(total_short, self.max_short)

        # Combine
        combined = {**longs, **shorts}
        net_exposure = sum(combined.values())

        # If net exposure exceeds limit, scale all weights down
        if abs(net_exposure) > self.net_limit:
            scale = self.net_limit / abs(net_exposure)
            for k in combined:
                combined[k] *= scale

        return combined

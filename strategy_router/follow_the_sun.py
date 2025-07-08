from global_hours.global_hours import GlobalMarketHours

class FollowTheSunRouter:
    def __init__(self, strategy_region_map):
        """
        Args:
            strategy_region_map: dict mapping strategy name → region (e.g., 'US', 'UK', 'JP', 'Crypto')
        """
        self.strategy_region_map = strategy_region_map
        self.market_status = GlobalMarketHours()

    def allocate(self, base_weights):
        """
        Adjusts strategy weights based on which regions are currently active.
        Args:
            base_weights: dict of strategy → base weight
        Returns:
            dict of strategy → adjusted weight
        """
        open_exchanges = self.market_status.get_open_exchanges()

        region_to_exchange = {
            "US": "NYSE",
            "UK": "LSE",
            "JP": "TSE",
            "EU": "LSE",
            "Futures": "CME",
            "Crypto": "Crypto"
        }

        adjusted_weights = {}
        for strategy, weight in base_weights.items():
            region = self.strategy_region_map.get(strategy, "US")
            exchange = region_to_exchange.get(region, "NYSE")

            if exchange in open_exchanges:
                adjusted_weights[strategy] = weight
            else:
                adjusted_weights[strategy] = weight * 0.2  # Downweight sleeping regions

        # Normalize
        total = sum(adjusted_weights.values())
        if total > 0:
            for k in adjusted_weights:
                adjusted_weights[k] /= total
        return adjusted_weights

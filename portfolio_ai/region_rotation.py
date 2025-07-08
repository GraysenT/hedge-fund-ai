from global_hours.global_hours import GlobalMarketHours

class RegionRotationEngine:
    def __init__(self, strategy_region_map):
        """
        Args:
            strategy_region_map (dict): maps strategy name → region name (e.g. {"US_Trend": "US"})
        """
        self.strategy_region_map = strategy_region_map
        self.market_status = GlobalMarketHours()

    def apply_region_rotation(self, base_weights):
        """
        Adjust weights based on which regions are active.
        Args:
            base_weights (dict): strategy → base weight
        Returns:
            dict: strategy → adjusted weight
        """
        exchange_status = self.market_status.get_exchange_status()

        adjusted_weights = {}
        for strategy, weight in base_weights.items():
            region = self.strategy_region_map.get(strategy, "US")
            exchange = self._map_region_to_exchange(region)

            # If market open, apply full weight; else downweight
            if exchange_status.get(exchange, False):
                adjusted_weights[strategy] = weight
            else:
                adjusted_weights[strategy] = weight * 0.3  # Downweight closed region

        # Normalize
        total = sum(adjusted_weights.values())
        if total > 0:
            for k in adjusted_weights:
                adjusted_weights[k] /= total
        return adjusted_weights

    def _map_region_to_exchange(self, region):
        return {
            "US": "NYSE",
            "UK": "LSE",
            "JP": "TSE",
            "EU": "LSE",
            "Futures": "CME",
            "Crypto": "Crypto"
        }.get(region, "NYSE")

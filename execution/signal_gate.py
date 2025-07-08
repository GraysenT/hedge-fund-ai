from global_hours.global_hours import GlobalMarketHours

class SignalGate:
    def __init__(self):
        self.market_hours = GlobalMarketHours()

        # Define which exchange maps to which asset prefix
        self.asset_exchange_map = {
            "US": "NYSE",
            "Futures": "CME",
            "UK": "LSE",
            "JP": "TSE",
            "Crypto": "Crypto"
        }

    def is_signal_allowed(self, signal):
        """
        Args:
            signal: dict with at least 'asset' or 'region' or 'type' keys
        Returns:
            bool: whether signal should be acted on
        """
        asset_type = signal.get("type", "").lower()
        region = signal.get("region", "")
        asset = signal.get("asset", "")

        # Map signal to exchange based on type or region
        if asset_type == "crypto":
            exchange = "Crypto"
        elif "fut" in asset_type or "future" in asset_type:
            exchange = "CME"
        elif region in self.asset_exchange_map:
            exchange = self.asset_exchange_map[region]
        elif "US" in asset:
            exchange = "NYSE"
        else:
            exchange = "NYSE"  # default fallback

        return self.market_hours.is_market_open(exchange)

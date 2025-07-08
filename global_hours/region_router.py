class RegionRouter:
    def __init__(self):
        self.region_keywords = {
            "US": ["SPY", "AAPL", "QQQ", "DJI", "_US", "NASDAQ", "NYSE"],
            "UK": ["FTSE", "BP", "BARC", "_UK", "LSE"],
            "JP": ["NIKKEI", "SONY", "TOYOTA", "_JP", "TSE"],
            "EU": ["DAX", "EURO", "_EU", "EUR"],
            "Crypto": ["BTC", "ETH", "SOL", "CRYPTO", "USDT", "USDC"]
        }

    def detect_region(self, signal):
        asset = signal.get("asset", "").upper()
        for region, keywords in self.region_keywords.items():
            if any(kw in asset for kw in keywords):
                return region
        return "Unknown"

class RegionMacroRegimeDetector:
    def __init__(self, thresholds=None):
        # Set default macro thresholds
        self.thresholds = thresholds or {
            "rate": 0.03,       # 3%
            "inflation": 0.04,  # 4%
            "growth": 0.0       # 0%
        }

    def classify(self, region_macro_data):
        """
        Args:
            region_macro_data (dict): maps region name → dict with 'interest_rate', 'inflation', 'gdp_growth'
        Returns:
            dict: region → regime label
        """
        regimes = {}
        for region, data in region_macro_data.items():
            rate = data.get("interest_rate", 0)
            inflation = data.get("inflation", 0)
            growth = data.get("gdp_growth", 0)

            if growth < self.thresholds["growth"]:
                regime = "recession"
            elif rate > self.thresholds["rate"] and inflation > self.thresholds["inflation"]:
                regime = "tightening"
            elif rate < self.thresholds["rate"] and inflation < self.thresholds["inflation"]:
                regime = "easing"
            else:
                regime = "neutral"

            regimes[region] = regime

        return regimes

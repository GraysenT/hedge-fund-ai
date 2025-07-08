import pandas as pd

class MacroRegimeDetector:
    def __init__(self, rate_thresh=0.03, inflation_thresh=0.04, growth_thresh=0.0):
        self.rate_thresh = rate_thresh          # e.g., 3% interest rate
        self.inflation_thresh = inflation_thresh  # e.g., 4% inflation
        self.growth_thresh = growth_thresh      # 0% GDP growth

    def classify(self, macro_data: dict):
        """
        Classifies macro regime.
        Args:
            macro_data: dict with keys: 'interest_rate', 'inflation', 'gdp_growth'
        Returns:
            str: one of ['tightening', 'easing', 'neutral', 'recession']
        """
        rate = macro_data.get('interest_rate', 0)
        inflation = macro_data.get('inflation', 0)
        growth = macro_data.get('gdp_growth', 0)

        if growth < self.growth_thresh:
            return "recession"
        elif rate > self.rate_thresh and inflation > self.inflation_thresh:
            return "tightening"
        elif rate < self.rate_thresh and inflation < self.inflation_thresh:
            return "easing"
        else:
            return "neutral"

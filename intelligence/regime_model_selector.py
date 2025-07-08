class RegimeModelSelector:
    def __init__(self):
        self.mapping = {
            "Growth": "LSTM",
            "Inflation": "MacroEdge",
            "Recession": "StatArb",
            "Neutral": "TrendAlpha"
        }

    def select(self, regime):
        model = self.mapping.get(regime, "LSTM")
        print(f"[MODEL SELECTOR] Regime: {regime} → Strategy: {model}")
        return model
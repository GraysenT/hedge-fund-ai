class RegimeSwitcher:
    def __init__(self):
        self.current_regime = None

    def detect_regime(self, macro_signals):
        if macro_signals.get("inflation") > 0.04:
            regime = "Inflationary"
        elif macro_signals.get("growth") < 0.01:
            regime = "Recession"
        elif macro_signals.get("volatility") > 0.25:
            regime = "Crisis"
        else:
            regime = "Neutral"

        if regime != self.current_regime:
            print(f"[REGIME SWITCH] {self.current_regime} → {regime}")
            self.current_regime = regime
        return self.current_regime
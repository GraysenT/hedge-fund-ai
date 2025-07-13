from datetime import datetime

class FusedForecast:
    def __init__(self, asset, short_term_sig, long_term_sig, macro_view, context_tags):
        self.asset = asset
        self.short = short_term_sig    # float: -1 to 1
        self.long = long_term_sig      # float: -1 to 1
        self.macro = macro_view        # float: -1 to 1
        self.contexts = context_tags   # list of strings
        self.timestamp = datetime.now().isoformat()
        self.conflict = abs(self.short - self.long)
        self.score = self.compute_score()

    def compute_score(self):
        base = (self.short * 0.4 + self.long * 0.4 + self.macro * 0.2)
        if self.conflict > 1.2:
            base *= 0.5  # suppress when conflict is high
        return round(base, 4)

    def to_dict(self):
        return {
            "asset": self.asset,
            "score": self.score,
            "contexts": self.contexts,
            "conflict": self.conflict,
            "timestamp": self.timestamp
        }
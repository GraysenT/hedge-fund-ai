class CapitalAtRisk:
    def __init__(self, max_short=0.4, max_net=1.0, max_gross=1.5):
        self.max_short = max_short
        self.max_net = max_net
        self.max_gross = max_gross

    def enforce(self, weighted_allocations: dict):
        signed_weights = weighted_allocations.copy()
        long_total = sum(v for v in signed_weights.values() if v > 0)
        short_total = -sum(v for v in signed_weights.values() if v < 0)
        net = long_total - short_total
        gross = long_total + short_total

        scale_factor = 1.0

        if short_total > self.max_short:
            scale_factor = min(scale_factor, self.max_short / short_total)
        if abs(net) > self.max_net:
            scale_factor = min(scale_factor, self.max_net / abs(net))
        if gross > self.max_gross:
            scale_factor = min(scale_factor, self.max_gross / gross)

        if scale_factor < 1.0:
            for k in signed_weights:
                signed_weights[k] *= scale_factor

        return signed_weights

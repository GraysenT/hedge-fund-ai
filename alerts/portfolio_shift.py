class PortfolioShiftNotifier:
    def __init__(self):
        self.last_weights = {}

    def check_for_change(self, new_weights):
        for strategy, new_weight in new_weights.items():
            old_weight = self.last_weights.get(strategy, None)
            if old_weight is not None and abs(new_weight - old_weight) > 0.05:
                self._send_alert(strategy, old_weight, new_weight)
        self.last_weights = new_weights

    def _send_alert(self, strategy, old, new):
        print(f"[ALERT] Allocation for {strategy} changed from {old:.2f} to {new:.2f}")
class SignalVeto:
    def __init__(self, regime):
        self.regime = regime  # one of 'low_vol', 'normal_vol', 'high_vol'

    def should_execute(self, signal):
        """
        Args:
            signal (dict): must include 'confidence' (0.0–1.0)
        Returns:
            bool: True if allowed, False if vetoed
        """
        confidence = signal.get('confidence', 0)

        # Rules based on volatility regime
        if self.regime == 'low_vol':
            return confidence >= 0.6
        elif self.regime == 'normal_vol':
            return confidence >= 0.5
        elif self.regime == 'high_vol':
            return confidence >= 0.75
        else:
            return False  # if regime unknown, block

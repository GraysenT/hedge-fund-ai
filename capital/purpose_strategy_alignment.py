class PurposeStrategyAlignment:
    def __init__(self):
        self.alignments = []

    def align_strategy_with_purpose(self, strategy_name, purpose):
        """Align a strategy with the system’s evolving purpose."""
        alignment = {"strategy": strategy_name, "purpose": purpose}
        self.alignments.append(alignment)
        print(f"Aligned strategy: {strategy_name} with purpose: {purpose}")
    
    def get_alignments(self):
        return self.alignments
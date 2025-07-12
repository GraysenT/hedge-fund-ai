class RecursiveCapitalGrowth:
    def __init__(self):
        self.growth_log = []

    def track_growth(self, amount, purpose):
        """Track capital growth in alignment with recursive purpose."""
        growth_entry = {"amount": amount, "purpose": purpose}
        self.growth_log.append(growth_entry)
        print(f"Tracked capital growth: {amount} for purpose: {purpose}")
    
    def get_growth_log(self):
        return self.growth_log
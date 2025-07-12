class CapitalFloorGuard:
    def __init__(self, capital_floor):
        self.capital_floor = capital_floor

    def check_allocation(self, allocation):
        if allocation < self.capital_floor:
            raise ValueError(f"Allocation {allocation} is below capital floor limit {self.capital_floor}")
        return allocation
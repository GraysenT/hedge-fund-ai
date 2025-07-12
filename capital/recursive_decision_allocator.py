class RecursiveDecisionAllocator:
    def __init__(self):
        self.allocations = []

    def allocate_decision(self, decision_name, decision_value):
        """Allocate resources based on recursive decision-making logic."""
        allocation = {"decision_name": decision_name, "value": decision_value}
        self.allocations.append(allocation)
        print(f"Allocated resources for decision: {decision_name} with value: {decision_value}")
    
    def get_allocations(self):
        return self.allocations
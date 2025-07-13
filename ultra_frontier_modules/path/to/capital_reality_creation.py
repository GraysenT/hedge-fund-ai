import json


class CapitalReality:

    def __init__(self):
        self.value_beliefs = {}
        self.symbolic_capital_flows = {}

    def simulate_value_belief(self, belief, value):
        self.value_beliefs[belief] = value
        return self.value_beliefs

    def influence_symbolic_capital_flow(self, capital_flow, influence):
        self.symbolic_capital_flows[capital_flow] = influence
        return self.symbolic_capital_flows

    def to_json(self):
        return json.dumps({'value_beliefs': self.value_beliefs, 'symbolic_capital_flows': self.symbolic_capital_flows})
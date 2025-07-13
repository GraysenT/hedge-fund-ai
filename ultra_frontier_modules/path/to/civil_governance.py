import json


class CivilGovernance:

    def __init__(self):
        self.policies = []
        self.decisions = []

    def implement_policy(self, policy):
        self.policies.append(policy)

    def make_decision(self, decision):
        self.decisions.append(decision)

    def get_policies(self):
        return self.policies

    def get_decisions(self):
        return self.decisions

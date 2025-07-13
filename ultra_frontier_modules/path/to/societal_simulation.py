import json
import random


class SocietalSimulation:

    def __init__(self):
        self.socioeconomic_systems = []
        self.policies = []
        self.decision_impact_frameworks = []

    def simulate(self):
        results = {}
        for system in self.socioeconomic_systems:
            results[system] = self.simulate_system(system)
        return results

    def simulate_system(self, system):
        return random.randint(0, 100)

    def add_system(self, system):
        self.socioeconomic_systems.append(system)

    def add_policy(self, policy):
        self.policies.append(policy)

    def add_decision_impact_framework(self, framework):
        self.decision_impact_frameworks.append(framework)

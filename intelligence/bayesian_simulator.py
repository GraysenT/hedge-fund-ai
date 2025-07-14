import random

def simulate_scenarios():
    scenarios = ['Bull Market', 'Bear Market', 'Stagflation']
    return random.choices(scenarios, k=3)
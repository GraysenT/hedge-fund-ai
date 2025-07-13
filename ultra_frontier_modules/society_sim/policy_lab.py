from .governance_simulator import SimulatedSociety

def run_policy_experiments(society, policy_options, n_trials=10):
    results = []
    for _ in range(n_trials):
        policy = {
            "tax_rate": random.uniform(*policy_options["tax_rate"]),
            "welfare_spending": random.uniform(*policy_options["welfare_spending"]),
            "edu_investment": random.uniform(*policy_options["edu_investment"]),
            "transparency_push": random.uniform(*policy_options["transparency_push"]),
        }
        test_society = SimulatedSociety(
            society.name, society.population, society.gdp_per_capita,
            society.corruption_index, society.education_index
        )
        test_society.apply_policy(policy)
        results.append((policy, test_society.summary()))
    return results
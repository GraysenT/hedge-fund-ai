import random

class SimulatedSociety:
    def __init__(self, name, population, gdp_per_capita, corruption_index, education_index):
        self.name = name
        self.population = population
        self.gdp_per_capita = gdp_per_capita
        self.corruption_index = corruption_index  # 0 (pure) to 1 (corrupt)
        self.education_index = education_index    # 0 to 1
        self.happiness = 0.5
        self.stability = 0.5

    def apply_policy(self, policy):
        """
        Policy is a dict with potential keys:
        'tax_rate', 'welfare_spending', 'edu_investment', 'transparency_push'
        """
        tax = policy.get("tax_rate", 0.2)
        welfare = policy.get("welfare_spending", 0.1)
        edu = policy.get("edu_investment", 0.1)
        transparency = policy.get("transparency_push", 0.0)

        # Simple simulated effects
        self.gdp_per_capita *= (1 - tax * 0.3 + welfare * 0.1 + edu * 0.2)
        self.education_index += edu * 0.05
        self.corruption_index *= (1 - transparency * 0.1)
        self.happiness += 0.1 * (welfare + edu) - 0.05 * tax
        self.stability += 0.05 * transparency + 0.05 * self.education_index

        self.happiness = min(max(self.happiness, 0), 1)
        self.stability = min(max(self.stability, 0), 1)

    def summary(self):
        return {
            "Society": self.name,
            "GDP per capita": round(self.gdp_per_capita, 2),
            "Corruption": round(self.corruption_index, 3),
            "Education Index": round(self.education_index, 3),
            "Happiness": round(self.happiness, 3),
            "Stability": round(self.stability, 3)
        }

def simulate_policy_effect():
    society = SimulatedSociety("Aurora", 1_000_000, 15000, 0.4, 0.6)
    policy = {
        "tax_rate": 0.25,
        "welfare_spending": 0.2,
        "edu_investment": 0.3,
        "transparency_push": 0.3
    }
    society.apply_policy(policy)
    return society.summary()

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_policy_effect())
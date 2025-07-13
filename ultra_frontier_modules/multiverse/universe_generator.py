import random
import uuid

class AlternateUniverse:
    def __init__(self, name, inflation, tech_adoption, war_risk, liquidity):
        self.id = str(uuid.uuid4())
        self.name = name
        self.inflation = inflation  # % annualized
        self.tech_adoption = tech_adoption  # 0–1
        self.war_risk = war_risk  # 0–1
        self.liquidity = liquidity  # normalized

    def summary(self):
        return {
            "Universe": self.name,
            "Inflation": self.inflation,
            "Tech Adoption": self.tech_adoption,
            "War Risk": self.war_risk,
            "Liquidity": self.liquidity
        }

def generate_universes(n=5):
    names = ["Terra-X", "Echo-7", "NeoValis", "ZetaPrime", "Cryon"]
    universes = []
    for _ in range(n):
        u = AlternateUniverse(
            name=random.choice(names) + "-" + str(random.randint(100,999)),
            inflation=round(random.uniform(-2, 15), 2),
            tech_adoption=round(random.uniform(0.1, 0.9), 3),
            war_risk=round(random.uniform(0.0, 1.0), 3),
            liquidity=round(random.uniform(0.3, 1.0), 3)
        )
        universes.append(u)
    return universes
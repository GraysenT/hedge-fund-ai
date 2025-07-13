from .civilization import Civilization
import random

def simulate_federation_round(civs):
    # Check for alliance formation
    for civ1 in civs:
        for civ2 in civs:
            if civ1.id != civ2.id:
                score = civ1.evaluate_alliance(civ2)
                if score > 0.4:
                    civ1.form_alliance(civ2)
                elif score < -0.3:
                    civ1.declare_enemy(civ2)

    # Trade between allies
    for civ in civs:
        for ally_id in civ.allies:
            ally = next(c for c in civs if c.id == ally_id)
            civ.trade(ally, random.randint(1, 5))

    return [civ.summary() for civ in civs]

def create_civilizations(n=5):
    names = ["Xenon", "Gaia", "Omicron", "Nova", "Valtari"]
    civs = []
    for _ in range(n):
        civ = Civilization(
            name=random.choice(names) + str(random.randint(100,999)),
            tech_level=random.uniform(0.4, 0.9),
            aggression=random.uniform(0.0, 1.0),
            cooperation=random.uniform(0.0, 1.0),
            resources=random.randint(10, 50)
        )
        civs.append(civ)
    return civs
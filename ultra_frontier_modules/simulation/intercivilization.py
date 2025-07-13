import random


class Civilization:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.technology_level = random.randint(1, 10)

    def interact(self, other):
        if self.technology_level > other.technology_level:
            self.population += other.population
            other.population = 0
        else:
            other.population += self.population
            self.population = 0


class Federation:
    def __init__(self, civilizations):
        self.civilizations = civilizations

    def resolve_conflicts(self):
        for i in range(len(self.civilizations)):
            for j in range(i + 1, len(self.civilizations)):
                self.civilizations[i].interact(self.civilizations[j])

    def simulate(self, rounds):
        for _ in range(rounds):
            self.resolve_conflicts()

import uuid
import random

class Civilization:
    def __init__(self, name, tech_level, aggression, cooperation, resources):
        self.id = str(uuid.uuid4())
        self.name = name
        self.tech = tech_level     # 0–1 scale
        self.aggression = aggression  # 0–1
        self.cooperation = cooperation  # 0–1
        self.resources = resources     # numeric pool
        self.allies = set()
        self.enemies = set()

    def evaluate_alliance(self, other):
        trust_factor = self.cooperation * other.cooperation
        fear_factor = self.aggression * other.aggression
        compatibility = trust_factor - fear_factor
        return compatibility

    def form_alliance(self, other):
        self.allies.add(other.id)
        other.allies.add(self.id)

    def declare_enemy(self, other):
        self.enemies.add(other.id)
        other.enemies.add(self.id)

    def trade(self, other, amount):
        if self.resources >= amount:
            self.resources -= amount
            other.resources += amount
            return True
        return False

    def summary(self):
        return {
            "Name": self.name,
            "Tech": self.tech,
            "Aggression": self.aggression,
            "Cooperation": self.cooperation,
            "Resources": self.resources,
            "Allies": list(self.allies),
            "Enemies": list(self.enemies)
        }
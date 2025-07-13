from .myth_generator import MythGenerator
from .culture_network import CultureNetwork
from .belief_network import BeliefNetwork


class IntelligenceCivilization:
    def __init__(self, myth_templates):
        self.myth_generator = MythGenerator(myth_templates)
        self.culture_network = CultureNetwork()
        self.belief_network = BeliefNetwork()

    def process_economic_event(self, event):
        myth = self.myth_generator.generate_myth(event)
        cultural_influence = self.culture_network.get_cultural_influence(event)
        belief_influence = self.belief_network.get_influence(event)
        return {'myth': myth, 'cultural_influence': cultural_influence, 'belief_influence': belief_influence}
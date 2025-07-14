from agents.archetypes.mythmaker import Mythmaker
from agents.archetypes.explorer import Explorer
from agents.archetypes.diplomat import Diplomat

def spawn(archetype_name):
    if archetype_name == "Mythmaker":
        return Mythmaker()
    elif archetype_name == "Explorer":
        return Explorer()
    elif archetype_name == "Diplomat":
        return Diplomat()
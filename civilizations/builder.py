from civilizations.agents.civic_agent import CivicAgent

def build_civilization(name):
    agents = [CivicAgent() for _ in range(5)]
    return {"name": name, "population": agents}
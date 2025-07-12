class MultiversalIdentity:
    def __init__(self):
        self.universes = []

    def add_universe(self, universe_name):
        """Expand the system across multiple universes."""
        self.universes.append(universe_name)
        print(f"Added universe: {universe_name}")
    
    def get_universes(self):
        return self.universes
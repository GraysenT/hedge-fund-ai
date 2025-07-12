class LatticeManager:
    def __init__(self):
        self.lattice = {}

    def add_to_lattice(self, agent_name, beliefs):
        """Manages all intelligence nodes and belief branches."""
        self.lattice[agent_name] = beliefs
        print(f"Added agent {agent_name} with beliefs: {beliefs}")

    def get_lattice(self):
        return self.lattice
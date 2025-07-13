import random

class MeshCoordinator:
    def __init__(self, node_name, peer_names):
        self.node_name = node_name
        self.peers = peer_names
        self.cycle = 0

    def elect_leader(self):
        all_nodes = self.peers + [self.node_name]
        return sorted(all_nodes)[self.cycle % len(all_nodes)]

    def next_cycle(self):
        self.cycle += 1
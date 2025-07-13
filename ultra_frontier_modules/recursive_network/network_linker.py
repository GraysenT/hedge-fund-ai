from .meta_memory_node import MetaMemoryNode

class RecursiveNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: MetaMemoryNode):
        self.nodes.append(node)

    def broadcast_insight(self, source_node, data):
        for node in self.nodes:
            if node.id != source_node.id:
                node.receive_insight(data)

    def sync_beliefs(self):
        states = [node.export_state() for node in self.nodes]
        for node in self.nodes:
            for state in states:
                if state["id"] != node.id:
                    node.import_state(state)
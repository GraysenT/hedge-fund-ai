import networkx as nx
from memory.strategy_lineage_graph import StrategyLineageGraph

class KnowledgeGraph:
    def __init__(self, lineage_graph: StrategyLineageGraph):
        self.graph = lineage_graph.graph

    def find_clusters(self):
        return list(nx.connected_components(self.graph.to_undirected()))

    def find_ancestors(self, node):
        return nx.ancestors(self.graph, node)

    def find_descendants(self, node):
        return nx.descendants(self.graph, node)

    def summarize(self):
        print(f"🧠 Graph Nodes: {len(self.graph.nodes)}")
        print(f"🧬 Edges: {len(self.graph.edges)}")
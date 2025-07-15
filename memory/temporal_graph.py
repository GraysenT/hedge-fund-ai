import networkx as nx

temporal_graph = nx.DiGraph()

def log_memory(agent_id, concept, timestamp):
    temporal_graph.add_node(concept, time=timestamp)
    temporal_graph.add_edge(agent_id, concept, time=timestamp)
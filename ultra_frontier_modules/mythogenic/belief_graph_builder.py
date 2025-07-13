import networkx as nx

def build_belief_graph(myths):
    """
    Constructs a directed belief graph from a list of myth or narrative objects.
    Each myth can contain: name, domain, influence_on, trust_score
    """
    G = nx.DiGraph()
    for myth in myths:
        G.add_node(myth["name"], domain=myth["domain"], trust=myth["trust_score"])
        for influence in myth.get("influence_on", []):
            G.add_edge(myth["name"], influence["target"], weight=influence["weight"])
    return G

def rank_influential_myths(G):
    """
    Ranks nodes by centrality and trust score to find dominant belief anchors.
    """
    centrality = nx.pagerank(G, weight="weight")
    ranked = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    return ranked
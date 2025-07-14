import networkx as nx

def get_lineage_graph():
    G = nx.DiGraph()
    G.add_edges_from([
        ("gen_strat_seed_a", "gen_strat_r4"),
        ("gen_strat_seed_b", "gen_strat_r2"),
    ])
    return G
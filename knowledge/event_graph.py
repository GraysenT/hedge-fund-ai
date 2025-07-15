G = {}
def add_edge(a, rel, b):
    G.setdefault(a, []).append((rel, b))

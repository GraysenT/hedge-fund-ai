def map_alpha_across_realities(alpha_results):
    """
    Scores alpha across simulations, synthetic timelines, and real-world regimes.
    """
    edge_map = {}
    for result in alpha_results:
        universe = result.get("universe", "real")
        edge = result.get("edge_score", 0)
        if universe not in edge_map:
            edge_map[universe] = []
        edge_map[universe].append(edge)
    return {k: sum(v) / len(v) for k, v in edge_map.items()}
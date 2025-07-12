def build_strategy_constellation_map(strategies):
    """
    Creates a network graph of strategies by type, logic similarity, and evolution path.
    """
    constellation = {}
    for strat in strategies:
        cluster = strat.get("class", "misc")
        if cluster not in constellation:
            constellation[cluster] = []
        constellation[cluster].append(strat["name"])
    return constellation
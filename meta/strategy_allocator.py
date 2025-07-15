def allocate(capital, strategies):
    return {s: capital / len(strategies) for s in strategies}
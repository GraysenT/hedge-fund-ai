def evolve_strategies(population):
    evolved = []
    for strategy in population:
        mutated = strategy.mutate()
        if mutated.evaluate() > strategy.evaluate():
            evolved.append(mutated)
        else:
            evolved.append(strategy)
    return evolved
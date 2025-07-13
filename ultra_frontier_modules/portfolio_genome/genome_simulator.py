from .genetic_pool import GeneticStrategyPool
from .gene_crossover_engine import crossover_strategies, mutate_config

def run_genetic_simulation():
    pool = GeneticStrategyPool()

    # Mock strategy configs
    strategy_a = {"window": 20, "threshold": 1.2, "leverage": 2.0}
    strategy_b = {"window": 10, "threshold": 0.8, "leverage": 1.5}

    pool.add_strategy("AlphaTrend", strategy_a, 0.77)
    pool.add_strategy("MeanRevert", strategy_b, 0.69)

    top = pool.sample_top_genes()
    new_config = crossover_strategies(top[0][1]["config"], top[1][1]["config"])
    mutated = mutate_config(new_config)

    return {
        "Parents": [top[0][1]["name"], top[1][1]["name"]],
        "New Strategy Config": mutated
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(run_genetic_simulation())
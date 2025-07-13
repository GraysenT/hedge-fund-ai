import random
from .genetic_encoder import encode_strategy_to_gene

class GeneticStrategyPool:
    def __init__(self):
        self.genes = {}

    def add_strategy(self, name, config, performance_score):
        gene = encode_strategy_to_gene(config)
        self.genes[gene] = {
            "name": name,
            "config": config,
            "score": performance_score
        }

    def sample_top_genes(self, top_n=3):
        return sorted(self.genes.items(), key=lambda x: x[1]['score'], reverse=True)[:top_n]
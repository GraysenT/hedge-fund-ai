import random

class StrategyMutator:
    def mutate(self, strategy_name):
        mutation_detail = f"param_shift_{random.randint(1, 100)}"
        new_strategy = f"{strategy_name}_mut{random.randint(1000,9999)}"
        print(f"[MUTATOR] {strategy_name} → {new_strategy} via {mutation_detail}")
        return new_strategy, mutation_detail
import random

def mutate(parent):
    return f"{parent}_mut{random.randint(1000,9999)}"

def simulate_evolution(root="gen_strat_seed", generations=5):
    lineage = {root: {"depth": 0, "sharpe": 0.1}}
    active = [root]

    for gen in range(1, generations + 1):
        new_gen = []
        for p in active:
            for _ in range(2):
                child = mutate(p)
                lineage[child] = {
                    "depth": gen,
                    "sharpe": round(lineage[p]["sharpe"] + random.uniform(-0.1, 0.3), 4)
                }
                new_gen.append(child)
        active = new_gen

    top = sorted(lineage.items(), key=lambda x: x[1]["sharpe"], reverse=True)[:5]
    print("🔮 Simulated Top Strategies:")
    for name, stats in top:
        print(f"{name}: Sharpe {stats['sharpe']}")

if __name__ == "__main__":
    simulate_evolution()
    
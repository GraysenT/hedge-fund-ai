from intelligence.autonomous_commander import AutonomousStrategyCommander
from core.strategy_performance import StrategyPerformance
from evolution.evolution_engine import EvolutionEngine

def run_meta_loop(strategies):
    tracker = StrategyPerformance()
    commander = AutonomousStrategyCommander(strategies, tracker)
    evolution = EvolutionEngine(strategies)

    # Simulate loop
    for i in range(100):
        # Simulate PnL feedback
        for s in strategies:
            reward = random.uniform(-0.5, 1.5)
            s.score(reward, sharpe=1.0)
            tracker.update(s.name, reward, 1.0)
        
        commander.evolve(evolution)

        if i % 10 == 0:
            print(f"[Meta AI] Current Focus:")
            for strat in commander.allocate_focus():
                print(f"  {strat.name} → Score: {strat.performance_score:.2f}")
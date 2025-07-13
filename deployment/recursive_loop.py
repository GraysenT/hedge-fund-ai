from agents.meta_coordinator import MetaCoordinator
from memory.strategy_lineage_graph import StrategyLineageGraph
import random

coordinator = MetaCoordinator()
lineage = StrategyLineageGraph()

def generate_mock_market_data():
    return {
        "price": random.uniform(100, 120),
        "ma": 110
    }

for t in range(200):
    data_map = {
        "equities": generate_mock_market_data(),
        "crypto": generate_mock_market_data(),
        "forex": generate_mock_market_data()
    }
    coordinator.run_step(data_map)

    if t % 50 == 0:
        snapshot = coordinator.global_strategy_snapshot()
        for market, agent_state in snapshot.items():
            for strat, score in agent_state["strategy_scores"].items():
                lineage.add_strategy(f"{market}-{strat}-{t}", score=score)

        coordinator.replicate_best()

lineage.visualize()
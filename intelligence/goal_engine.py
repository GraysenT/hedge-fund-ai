import random

class GoalEngine:
    def __init__(self, base_mission="maximize_roi"):
        self.goal = base_mission
        self.history = []

    def mutate_goal(self):
        mutations = [
            "minimize_drawdown",
            "increase_stability",
            "dominate_market",
            "cooperate_with_agents",
            "discover_new_strategies"
        ]
        new_goal = random.choice(mutations)
        self.history.append((self.goal, new_goal))
        self.goal = new_goal

    def evaluate_alignment(self, performance_metrics: dict) -> float:
        if "roi" in self.goal:
            return performance_metrics.get("roi", 0)
        if "drawdown" in self.goal:
            return -performance_metrics.get("drawdown", 0)
        return random.uniform(0, 1)
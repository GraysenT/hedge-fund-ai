import random
from evolution.rl_controller import RLController
from strategies.trend_following import TrendFollowingStrategy
from strategies.mean_reversion import MeanReversionStrategy

strategies = [
    TrendFollowingStrategy("Trend", {"base": 1}),
    MeanReversionStrategy("Mean", {"base": 1})
]
controller = RLController(strategies)

def simulate_market():
    return random.choice(["buy", "sell", "hold"]), random.uniform(-1, 1)

for step in range(100):
    strategy = controller.select()
    action, reward = simulate_market()
    controller.update(strategy.name, reward)
    print(f"[Step {step}] Strategy: {strategy.name} | Action: {action} | Reward: {reward:.2f}")
from societies.city_state import CityStateNode
from agents.recursive_agent import RecursiveAgent
import time

eth_node = CityStateNode("ETHUSD")
eth_node.register_agent("guardian.eth")

agent = RecursiveAgent("ETHUSD")
for _ in range(1000000):
    market_data = {"price": 1800, "ma": 1750}
    agent.step(market_data)
    eth_node.update_agent("guardian.eth", +0.5)
    eth_node.save()
    time.sleep(10)
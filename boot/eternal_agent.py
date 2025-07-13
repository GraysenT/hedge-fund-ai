from dream.dream_engine import DreamEngine
from oracle.satellite_oracle import SatelliteOracle
from societies.social_graph import SocialCapitalGraph
from societies.city_state import CityStateNode

agent = "agent.zeta"
city = CityStateNode("ETHUSD")
oracle = SatelliteOracle()
dreamer = DreamEngine(agent)
graph = SocialCapitalGraph()

# Register agent
city.register_agent(agent)

# Dream future
dream = dreamer.dream_tick({"price": 2000})
print(f"💭 {agent} dreamed: {dream}")

# Oracle prediction
forecast = oracle.forecast("ETH will")
print(f"📡 Oracle says: {forecast}")

# Social bonding
graph.interact(agent, "agent.gamma", value=0.8)
graph.visualize()

# Persist
city.update_agent(agent, +42)
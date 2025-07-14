import sys
import os
import time

# Ensure root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from societies.city_state import CityStateNode
from agents.recursive_agent import RecursiveAgent

MARKET = "ETHUSD"
AGENT_NAME = "guardian.eth"

print("🚀 Starting city-state agent for:", MARKET)

# Create or load city-state
try:
    eth_node = CityStateNode(MARKET)
    if AGENT_NAME not in eth_node.agent_registry:
        eth_node.register_agent(AGENT_NAME)
        print(f"✅ Registered new agent: {AGENT_NAME}")
    else:
        print(f"🔁 Loaded existing agent: {AGENT_NAME}")
except Exception as e:
    print(f"❌ Error initializing city-state: {e}")
    sys.exit(1)

# Create recursive trading agent
try:
    agent = RecursiveAgent(MARKET)
    print("🧠 Recursive agent initialized.")
except Exception as e:
    print(f"❌ Failed to initialize agent: {e}")
    sys.exit(1)

# Main loop
tick = 1
try:
    while True:
        print(f"⏱ Tick {tick}...")

        market_data = {"price": 1800, "ma": 1750}  # placeholder mock feed
        try:
            agent.step(market_data)
        except Exception as step_err:
            print(f"⚠️ Error in agent step: {step_err}")

        try:
            eth_node.update_agent(AGENT_NAME, +0.5)
            eth_node.save()
        except Exception as save_err:
            print(f"⚠️ Error saving state: {save_err}")

        time.sleep(1)
        tick += 1

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")

except Exception as crash:
    print(f"🔥 Critical error in city loop: {crash}")
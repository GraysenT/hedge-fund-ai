import time
import random
from alerts.alert_sender import send_telegram
send_telegram(f"🔁 Forked agent {agent.name} with Sharpe {agent.sharpe_score}")

from registry.agent_registry import AgentRegistry

def run_evolution_loop():
    while True:
        try:
            print("🧬 Evolution: scanning agents...")
            top_agents = AgentRegistry.get_top_agents(metric="sharpe", threshold=0.2)

            for agent in top_agents:
                new_config = {
                    "mutation_seed": random.randint(0, 10000),
                    "window": random.choice([10, 20, 30])
                }
                print(f"🧬 Evolving {agent.name} → new config: {new_config}")
                agent.set_params(new_config)

            time.sleep(60)
        except Exception as e:
            print(f"❌ Evolution error: {e}")
            time.sleep(10)
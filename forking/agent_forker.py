import time
from registry.agent_registry import AgentRegistry
import copy
import random
from alerts.alert_sender import send_telegram
send_telegram(f"🔁 Forked agent {agent.name} with Sharpe {agent.sharpe_score}")

def agent_fork_loop():
    while True:
        try:
            print("🤖 Forking: checking agent performance...")
            for agent in AgentRegistry.all():
                if hasattr(agent, "sharpe_score") and agent.sharpe_score < 0:
                    fork = copy.deepcopy(agent)
                    fork.name = f"{agent.name}_forked"
                    fork.set_params({"mutation_factor": random.uniform(0.9, 1.1)})
                    AgentRegistry.register(fork.name, fork)
                    print(f"🔁 Forked agent: {fork.name}")
            time.sleep(120)
        except Exception as e:
            print(f"❌ Forking error: {e}")
            time.sleep(30)
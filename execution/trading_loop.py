import time
from registry.agent_registry import AgentRegistry

def run_live_trading():
    while True:
        try:
            for agent in AgentRegistry.all():
                signal = agent.get_signal({"price": 101, "moving_average": 100, "momentum": 1})  # Stub
                print(f"💹 {agent.name} → Signal: {signal}")
            time.sleep(30)
        except Exception as e:
            print(f"❌ Trading loop error: {e}")
            time.sleep(10)
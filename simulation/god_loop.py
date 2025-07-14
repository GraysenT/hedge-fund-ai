import os
import sys
import time
import json
import random
from datetime import datetime

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.meta_coordinator import MetaCoordinator
from evolution.recursive_architect import EvolutionArchitect
from simulation.forking_simulator import ForkingSimulator
from dream.dream_engine import DreamEngine
from dream_to_signal import interpret_dream
from oracle.meta_oracle import ask_oracle
from utils.telegram_bot import send_telegram

class GodLoop:
    def __init__(self):
        self.tick = 0
        self.coordinator = MetaCoordinator()
        self.architect = EvolutionArchitect()
        self.forker = ForkingSimulator()
        self.dreamer = DreamEngine("god_agent")

        os.makedirs("logs", exist_ok=True)

    def log_brain_entry(self, dream, signal, oracle_feedback):
        log_entry = {
            "tick": self.tick,
            "dream": dream,
            "signal": signal,
            "oracle": oracle_feedback
        }
        with open("logs/brain.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def log_dream(self, dream):
        with open("logs/dreams.jsonl", "a") as f:
            f.write(json.dumps(dream) + "\n")

    def log_fork(self, sim_id, parent_id="root"):
        with open("logs/forks.jsonl", "a") as f:
            f.write(json.dumps({
                "sim": sim_id,
                "tick": self.tick,
                "parent": parent_id,
                "timestamp": datetime.utcnow().isoformat()
            }) + "\n")

    def run(self):
        print("🧠 GodLoop is starting...")

        while True:
            self.tick += 1

            # Simulate dynamic market data
            market_data = {
                "equities": {"price": random.uniform(90, 110), "ma": 100},
                "crypto": {"price": random.uniform(1700, 2300), "ma": 2000}
            }

            self.coordinator.run_step(market_data)

            # Dream every 3 ticks
            if self.tick % 3 == 0:
                dream = self.dreamer.dream_tick(market_data["crypto"])
                dream["tick"] = self.tick
                dream["context"]["timestamp"] = datetime.utcnow().isoformat()

                signal = interpret_dream(dream)
                oracle_feedback = "🧠 Oracle offline (quota exceeded)."

                print(f"💭 Tick {self.tick} Dream: signal={signal} | future={dream['future_price']}")
                print(f"🔮 Oracle: {oracle_feedback}")

                self.log_dream(dream)
                self.log_brain_entry(dream, signal, oracle_feedback)

                send_telegram(f"💭 Tick {self.tick} dream: {signal.upper()} — {oracle_feedback}")

                # Optional: feed signal to live agent
                agent = self.coordinator.agents["crypto"]
                if hasattr(agent, "manual_signal"):
                    agent.manual_signal = signal

            # Fork simulation every 10 ticks
            if self.tick % 10 == 0:
                sim_id = self.forker.fork(
                    agent_state=self.coordinator.agents["crypto"],
                    market_state=market_data["crypto"]
                )
                self.log_fork(sim_id)
                print(f"🌱 Forked sim: {sim_id}")

            # Evolve evolution every 5 ticks
            if self.tick % 5 == 0:
                plan = self.architect.get_latest_plan() or {
                    "mutation_rate": 0.05,
                    "selection_pressure": 0.3,
                    "diversity_bias": 0.2
                }
                new_plan = self.architect.evolve_evolution(plan)
                print(f"🔁 Evolved evolution plan: {new_plan}")

            time.sleep(1)

if __name__ == "__main__":
    loop = GodLoop()
    loop.run()
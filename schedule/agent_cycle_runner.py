import subprocess
import time
from datetime import datetime

def run_cycle():
    print("🔁 Starting daily agent evolution cycle...")

    subprocess.call(["python3", "-m", "agents.agent_registry"])
    subprocess.call(["python3", "-m", "agents.agent_tournament"])
    subprocess.call(["python3", "-m", "agents.agent_mutator"])
    subprocess.call(["python3", "-m", "risk_control.agent_retirement"])

    print("✅ Agent evolution complete.\n")

if __name__ == "__main__":
    while True:
        now = datetime.now()
        if now.hour == 22 and now.minute == 0:  # Run at 10:00 PM
            run_cycle()
            time.sleep(60)
        else:
            time.sleep(30)
    
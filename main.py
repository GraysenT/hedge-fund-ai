import threading
import time
import os
import subprocess

# === Port Cleanup ===
def free_ports(ports):
    for port in ports:
        try:
            pids = subprocess.check_output(["lsof", "-ti", f":{port}"]).decode().strip().split("\n")
            for pid in pids:
                if pid:
                    print(f"🔪 Killing PID {pid} on port {port}")
                    os.system(f"kill -9 {pid}")
        except subprocess.CalledProcessError:
            pass  # Port not in use

    # 🔪 Extra: kill any zombie streamlit processes just in case
    os.system("pkill -f streamlit")

# === Thread Targets ===
from orchestrator.api_runner import start_api
from dashboard.main import start_dashboard
from evolution.loop import run_evolution_loop
from forking.agent_forker import agent_fork_loop
from execution.trading_loop import run_live_trading

def log_system_status():
    while True:
        print("✅ System heartbeat - all threads active")
        time.sleep(30)

if __name__ == "__main__":
    # 🚫 Kill previous runs on required ports
    free_ports([8000, 8500])

    threads = []

    threads.append(threading.Thread(target=start_api, name="FastAPI"))
    threads.append(threading.Thread(target=start_dashboard, name="Dashboard"))
    threads.append(threading.Thread(target=run_evolution_loop, name="Evolution"))
    threads.append(threading.Thread(target=agent_fork_loop, name="Forking"))
    threads.append(threading.Thread(target=run_live_trading, name="Trading"))
    threads.append(threading.Thread(target=log_system_status, name="Heartbeat"))

    for t in threads:
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)
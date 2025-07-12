import subprocess
import time

CRITICAL_MODULES = {
    "runloop.py": "python3 runloop.py",
    "evolve.py": "python3 evolve.py"
}

def monitor_and_restart():
    while True:
        for name, cmd in CRITICAL_MODULES.items():
            try:
                result = subprocess.run(["pgrep", "-f", name], capture_output=True)
                if not result.stdout:
                    print(f"[Self-Heal] Restarting {name}")
                    subprocess.Popen(cmd.split())
            except Exception as e:
                print(f"[Self-Heal Error] {e}")
        time.sleep(60)

if __name__ == "__main__":
    monitor_and_restart()
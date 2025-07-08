import os
import time
from subprocess import run

CHECKPOINT = "memory/meta_blended_weights.csv"

def monitor_and_restart():
    while True:
        if not os.path.exists(CHECKPOINT):
            print("🛠️ Critical file missing. Restarting system loop...")
            run(["python3", "runloop.py"])  # or restart docker service
        time.sleep(60)  # check every 60 seconds
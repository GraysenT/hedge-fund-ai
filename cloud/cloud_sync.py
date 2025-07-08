import os
import subprocess
from datetime import datetime

REMOTE = "Cloud_Trading"
FOLDERS = ["snapshots", "execution_logs", "memory"]

def sync_to_cloud():
    for folder in FOLDERS:
        local_path = f"./{folder}"
        remote_path = f"{REMOTE}:/hedge_fund_ai/{folder}"
        print(f"☁️ Syncing {local_path} → {remote_path} ...")
        result = subprocess.run(["rclone", "sync", local_path, remote_path, "-v"], capture_output=True)
        print(result.stdout.decode())

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"✅ Cloud sync completed at {timestamp}")
    
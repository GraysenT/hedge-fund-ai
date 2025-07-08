import subprocess

FOLDERS = ["execution_logs", "performance_logs", "snapshots", "memory", "audit"]
REMOTE = "Cloud_Trading:/hedge_fund_ai_full"

def sync_all():
    for folder in FOLDERS:
        subprocess.run(["rclone", "sync", folder, f"{REMOTE}/{folder}", "-v"])
    print("✅ All audit and live folders synced to S3.")
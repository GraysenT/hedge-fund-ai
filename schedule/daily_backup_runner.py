import os
import time
from datetime import datetime
from cloud.aws_uploader import upload_to_s3

FILES_TO_BACKUP = [
    "strategy_memory/strategy_lineage.json",
    "strategy_memory/deployment_status.json"
]

FOLDERS_TO_BACKUP = [
    "memory/scaled_allocations",
    "memory/order_logs",
    "memory/performance"
]

def backup_all():
    timestamp = datetime.now().strftime("%Y-%m-%d")
    for file in FILES_TO_BACKUP:
        if os.path.exists(file):
            key = f"backups/{timestamp}/{os.path.basename(file)}"
            upload_to_s3(file, key)

    for folder in FOLDERS_TO_BACKUP:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                full_path = os.path.join(folder, file)
                s3_key = f"backups/{timestamp}/{folder.replace('/', '_')}/{file}"
                upload_to_s3(full_path, s3_key)

if __name__ == "__main__":
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute == 0:  # 8:00 PM backup
            backup_all()
            time.sleep(60)
        else:
            time.sleep(30)
            
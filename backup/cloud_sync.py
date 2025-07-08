import boto3
import os
from datetime import datetime

S3_BUCKET = "cloud-trading-backup"
PREFIX = "hedge_ai_snapshots"
LOCAL_DIRS = ["logs", "memory", "reports"]

def backup_to_s3():
    s3 = boto3.client("s3")
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    for directory in LOCAL_DIRS:
        for root, _, files in os.walk(directory):
            for f in files:
                path = os.path.join(root, f)
                key = f"{PREFIX}/{timestamp}/{path}"
                try:
                    s3.upload_file(path, S3_BUCKET, key)
                    print(f"☁️ Uploaded: {path} → {key}")
                except Exception as e:
                    print(f"❌ Failed: {path} → {e}")

if __name__ == "__main__":
    backup_to_s3()
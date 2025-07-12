import boto3
import os

s3 = boto3.client('s3')
BUCKET = "cloud_trading_snapshots"

def upload_snapshot(file_path, s3_path=None):
    if not s3_path:
        s3_path = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, BUCKET, s3_path)
        print(f"[Backup] Uploaded {file_path} to S3:{s3_path}")
    except Exception as e:
        print(f"[Backup] Failed: {e}")
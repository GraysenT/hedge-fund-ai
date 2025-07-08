import os
import boto3
from datetime import datetime

from utils.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BACKUP_S3_BUCKET_NAME


def upload_to_s3(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Snapshot not found: {file_path}")

    filename = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    s3_key = f"snapshots/{timestamp}_{filename}"

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    try:
        s3.upload_file(file_path, BACKUP_S3_BUCKET_NAME, s3_key)
        print(f"✅ Snapshot uploaded to S3: s3://{BACKUP_S3_BUCKET_NAME}/{s3_key}")
    except Exception as e:
        print(f"❌ S3 upload failed: {e}")


if __name__ == '__main__':
    test_path = "strategy_memory/latest_snapshot.pkl"
    upload_to_s3(test_path)

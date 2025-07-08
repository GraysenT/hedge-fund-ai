import shutil
import os
import boto3
from datetime import datetime

BACKUP_FOLDER = "backup_zips"
AWS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET_KEY")
BUCKET = os.getenv("BACKUP_S3_BUCKET_NAME")

def zip_backup():
    now = datetime.now().strftime("%Y-%m-%d_%H%M")
    zip_path = f"{BACKUP_FOLDER}/backup_{now}.zip"
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    shutil.make_archive(zip_path.replace(".zip", ""), "zip", "memory")
    return zip_path

def upload_to_s3(file_path):
    s3 = boto3.client("s3", aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)
    s3.upload_file(file_path, BUCKET, f"archives/{os.path.basename(file_path)}")
    print(f"☁️ Uploaded to s3://{BUCKET}/archives/{os.path.basename(file_path)}")

if __name__ == "__main__":
    path = zip_backup()
    upload_to_s3(path)

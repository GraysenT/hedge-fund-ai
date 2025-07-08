import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET_KEY")
BUCKET = os.getenv("BACKUP_S3_BUCKET_NAME")

def upload_to_s3(local_path, s3_key):
    s3 = boto3.client('s3', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)
    try:
        s3.upload_file(local_path, BUCKET, s3_key)
        print(f"☁️ Uploaded {local_path} to s3://{BUCKET}/{s3_key}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        
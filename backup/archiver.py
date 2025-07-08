import zipfile
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def zip_data(output_name="system_snapshot.zip"):
    folders = ["memory", "models", "strategy_memory", "plugins"]
    with zipfile.ZipFile(output_name, "w") as zipf:
        for folder in folders:
            for root, _, files in os.walk(folder):
                for file in files:
                    path = os.path.join(root, file)
                    zipf.write(path)
    print(f"✅ Archived system to {output_name}")
    return output_name

def upload_to_s3(zip_path):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
    )
    bucket = os.getenv("BACKUP_S3_BUCKET_NAME")
    key = f"backups/{datetime.now().strftime('%Y-%m-%d')}_{zip_path}"
    s3.upload_file(zip_path, bucket, key)
    print(f"☁️ Uploaded to S3: s3://{bucket}/{key}")

if __name__ == "__main__":
    path = zip_data()
    upload_to_s3(path)
    
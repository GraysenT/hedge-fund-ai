import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "your-access-key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "your-secret-key")
BACKUP_S3_BUCKET_NAME = os.getenv("BACKUP_S3_BUCKET_NAME", "your-s3-bucket-name")

# Optional: hardcoded fallback (remove after testing)
# AWS_ACCESS_KEY = "ABC123..."
# AWS_SECRET_KEY = "XYZ456..."
# BACKUP_S3_BUCKET_NAME = "my-strategy-snapshots"
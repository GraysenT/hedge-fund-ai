import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
)

def upload_to_s3(local_file, s3_key):
    s3 = session.client('s3')
    s3.upload_file(local_file, os.getenv("BACKUP_S3_BUCKET_NAME"), s3_key)
    print(f"☁️ Uploaded to S3: {s3_key}")

def launch_ec2_instance():
    ec2 = session.resource("ec2")
    instance = ec2.create_instances(
        ImageId="ami-0a91cd140a1fc148a",  # Ubuntu
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.medium",
        KeyName="your-key",
        SecurityGroups=["your-security-group"]
    )
    print(f"🚀 Launched EC2: {instance[0].id}")

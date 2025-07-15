# Define EC2 setup
INSTANCE_TYPE="t2.medium"
AMI="ami-0abcdef1234567890"  # Choose a FastAPI/Ubuntu-optimized AMI
KEY_NAME="hedge-key"
SECURITY_GROUP="hedge-sg"

# Launch
aws ec2 run-instances \
  --image-id $AMI \
  --count 1 \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-groups $SECURITY_GROUP \
  --user-data file://deploy/setup-instance.sh
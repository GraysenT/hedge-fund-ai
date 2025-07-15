INSTANCE_TYPE="t2.medium"
AMI_ID="ami-0abcdef1234567890"  # Replace with your region’s latest Ubuntu AMI
KEY_NAME="hedge-key"
SECURITY_GROUP="hedge-sg"

aws ec2 run-instances \
  --image-id $AMI_ID \
  --count 1 \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-groups $SECURITY_GROUP \
  --user-data file://deploy/setup-instance.sh
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "graviton_fund_node" {
  ami           = "ami-0c1a7f89451184c8b"  # ARM-based Ubuntu
  instance_type = "c7g.medium"            # Graviton v3
  key_name      = "your-key"
  tags = {
    Name = "Graviton-Fund-Node"
  }
}

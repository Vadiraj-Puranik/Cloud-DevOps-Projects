resource "aws_vpc" "private" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main-vpc"
  }
}


resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.private.id
  cidr_block = "10.0.1.0/24"
}

output "vpc_id"{
  value = aws_vpc.private.id
}

output "subnet_id"{
  value = aws_subnet.private.id
}


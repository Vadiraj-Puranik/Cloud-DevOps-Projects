module "vpc"{
  source = "../VPC"
}

resource "aws_instance" "appserver" {
  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  availability_zone = "us-east-1"
  vpc_security_group_ids = [module.vpc.vpc_id]
  subnet_id =  [module.vpc.subnet_id]
  key_name = "devops-projects.pem"
}

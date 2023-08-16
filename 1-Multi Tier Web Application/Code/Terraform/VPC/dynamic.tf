variable "security_group_ports" {
  type  = list(number)
  value = [22, 443, 80]
}



resource "aws_security_group" "public" {
  name = "public-security_group"

  dynamic "ingress" {
    for_each = var.security_group_ports
    content {
      from_port = ingress.value
      to_port   = ingress.value
      protocol  = "tcp"
    }
  }

  dynamic "egress" {
    for_each = var.security_group_ports
    content {
      from_port = ingress.value
      to_port   = ingress.value
      protocol  = "tcp"
    }
  }

}
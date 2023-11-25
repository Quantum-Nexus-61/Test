provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI ID
  instance_type = "t2.micro"

  // Generate a new SSH key pair
  key_name = aws_key_pair.generated_key.key_name

  user_data = <<-EOF
              #!/bin/bash
              sudo su
              yum update -y
              yum install -y httpd
              cd /var/www/html
              wget https://github.com/Quantum-Nexus-61/Dev/archive/refs/heads/main.zip
              unzip Dev-main.zip
              cp -r Dev-main/* /var/www/html/
              rm -rf Dev-main.zip
              systemctl enable httpd 
              systemctl start httpd
              EOF
}

resource "aws_key_pair" "generated_key" {
  key_name   = "example-key"
  public_key = file("~/.ssh/id_rsa.pub")  # Use the public key from your local machine
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}

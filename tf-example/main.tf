provider "aws" {
  region  = "us-east-2"
}

terraform {
  backend "s3" {
      bucket = "sohan-1230987"
      key    = "build/terraform.tfstate"
      region = "us-east-2"
  }
}

resource "aws_s3_bucket" "s3Bucket" {
     bucket = "sohan-138923712"
     acl       = "private"

   website {
       index_document = "index.html"
   }
}

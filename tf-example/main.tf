provider "aws" {
  region  = "ap-south-1"
}

terraform {
  backend "s3" {
      bucket = "sohan-1230987"
      key    = "build/terraform.tfstate"
      region = "us-east-2"
  }
}

data "aws_iam_policy_document" "website_policy" {
  statement {
    actions = [
      "s3:GetObject"
    ]
    principals {
      identifiers = ["*"]
      type = "AWS"
    }
    resources = [
      "arn:aws:s3:::gotrav/*"
    ]
  }
}

resource "aws_s3_bucket" "s3Bucket" {
     bucket = "website"
     acl       = "public-read"

     policy = data.aws_iam_policy_document.website_policy.json

   website {
       index_document = "index.html"
   }
}

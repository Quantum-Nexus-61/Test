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
     bucket = "website"
     acl       = "public-read"

    policy  = <<EOF
    {
         "id" : "MakePublic",
       "version" : "2023-11-25",
       "statement" : [
          {
             "action" : [
                 "s3:GetObject"
              ],
             "effect" : "Allow",
             "resource" : "arn:aws:s3:::website/*",
             "principal" : "*"
          }
        ]
      }
    EOF

   website {
       index_document = "index.html"
   }
}

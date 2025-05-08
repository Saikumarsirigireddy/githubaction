import boto3
import os
import time
github_run_number = os.getenv("GITHUB_RUN_NUMBER")  

lambda_client = boto3.client("lambda", verify=False)

function_name = f"lambda-container-fn-{int(time.time())}" 
image_uri = f"339713111450.dkr.ecr.us-east-1.amazonaws.com/demo-repo:{github_run_number}"  
role_arn = "arn:aws:iam::339713111450:role/lambda-ecr"


response = lambda_client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=role_arn
)

# Print response from AWS
print(response)
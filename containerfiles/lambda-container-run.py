import boto3
import os

# Get the GitHub Run Number from the environment variable
github_run_number = os.getenv("GITHUB_RUN_NUMBER", "latest")  # Defaults to 'latest' if not set

# Create AWS Lambda client
lambda_client = boto3.client("lambda", verify=False)

# Define function details
function_name = "lambda-container-fn:{github_run_number}"
image_uri = f"339713111450.dkr.ecr.us-east-1.amazonaws.com/demo-repo:{github_run_number}"  # Dynamic image URI
role_arn = "arn:aws:iam::339713111450:role/lambda-ecr"

# Create Lambda function with container image
response = lambda_client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=role_arn
)

# Print response from AWS
print(response)
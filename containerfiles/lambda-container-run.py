import boto3

# Create AWS Lambda client
lambda_client = boto3.client("lambda",verify=False)

# Define function details
function_name = "lambda-container-fn"
image_uri = "339713111450.dkr.ecr.us-east-1.amazonaws.com/demo-repo:latest"
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
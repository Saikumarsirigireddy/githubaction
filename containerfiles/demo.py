import boto3
from pprint import pprint
# Start a session
aws_management_console = boto3.Session(profile_name="default")

# Create an IAM client with SSL verification disabled
iam_client = aws_management_console.client("iam", verify=False)

# Get user details
result=iam_client.list_users()
for i in result["Users"]:
    print(i["UserName"])

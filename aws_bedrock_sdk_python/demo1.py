import boto3
import json
import os
import botocore
from botocore.config import Config


# Make sure you're using a region that is supporting BedRock
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


# Update boto3.client to take into account the config
bedrock = boto3.client(service_name="bedrock")
bedrock_runtime = boto3.client(service_name="bedrock-runtime")

models_list = bedrock.list_foundation_models()

model_json = json.dumps(models_list)  # models_list is  Python dictonary that needs converting to json 
print(model_json)


# Make sure your account is authorized to use the models

prompt_data = """Command: Write me a blog about making strong business decisions as a leader.

Blog:
"""

try:
    
    body = json.dumps({"inputText": prompt_data})
    modelId = "amazon.titan-text-express-v1"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType,
    )
    response_body = json.loads(response.get("body").read())

    print(response_body.get("results")[0].get("outputText"))

except botocore.exceptions.ClientError as error:
    
    if error.response['Error']['Code'] == 'AccessDeniedException':
           print(f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubeshoot this issue please refer to the following resources.\
                 \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                 \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
        
    else:
        raise error

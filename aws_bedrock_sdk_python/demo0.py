import boto3
import json
import os

# Make sure you're using a region that is supporting BedRock
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


# Update boto3.client to take into account the config
bedrock = boto3.client(service_name="bedrock")
bedrock_runtime = boto3.client(service_name="bedrock-runtime")

models_list = bedrock.list_foundation_models()

model_json = json.dumps(models_list)  # models_list is  Python dictonary that needs converting to json 
print(model_json)

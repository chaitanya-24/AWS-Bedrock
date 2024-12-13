import boto3
import json

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Model payload
payload = {
    "prompt": "<s>[INST] Write a short poem about AI [/INST]",
    "max_tokens": 200,
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50
}

# Prepare request body
body = json.dumps(payload)

# Invoke the model directly using modelId
response = bedrock.invoke_model(
    modelId="mistral.mistral-7b-instruct-v0:2",
    body=body,
    accept="application/json",
    contentType="application/json"
)

# Parse and print response
response_body = json.loads(response.get("body").read())
print(json.dumps(response_body, indent=4))
# print(json.dumps(response_body['outputs'][0]['text']))

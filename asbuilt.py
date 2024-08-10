# Use the Converse API to send a text message to Titan Text G1 - Premier.

import boto3
from botocore.exceptions import ClientError


boto3.setup_default_session(profile_name='audaz')


# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

# Start a conversation with the user message.
user_message = """Act like you are a DevOps Engeneer in the tecnology organization at XPTO company. Generate a technical as-built document of a client XPTO cloud infrastructure.
The customer that is owner of the infraestruct is XCorp.


Bellow are the Cloud Native services that is used by the Customer:

- Kubernetes
- KEDA
- Ngnix Ingress Controller
- AWS CloudFront
- AWS S3
- AWS ECR
- AWS Router53
- Oracle CLoud Instance
- Rabbitmq
- Redis for cache
- MySQL Heatwave
- Postgres Database
- ElasticSearch for logging and APM
- PRTG


 - Keep the overall length of the document to less than 3000 words
 - Craft a punchy headline to indulge people to read the document
 - Use the text in third person


    """



structure="""
 - Structure of the AS-BUILT in 5 sections with markdown headings as mentioned:
 - ## Introduction:
 - ## Problem Statement:
 - ## Why it matters:
 - ## Solution:
 - ## Conclusion:
 """

conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId="amazon.titan-text-premier-v1:0",
        messages=conversation,
        inferenceConfig={"maxTokens":1024,"stopSequences":[],"temperature":0.7,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
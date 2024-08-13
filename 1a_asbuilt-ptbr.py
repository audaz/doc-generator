# Use the Converse API to send a text message to Titan Text G1 - Premier.

import boto3
from botocore.exceptions import ClientError


boto3.setup_default_session(profile_name='audaz')


# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

# Start a conversation with the user message.

# user_prompt=''
# with open("dna.txt", "r") as file:
#     user_prompt = file.read().replace("\n", "")
# print(user_prompt)

# will print ATCAGTGGAAACCCAGTGCTAGAGGATGGAATGACCTTAAATCAGGGACGATATTAAACGGAA


user_message = """Aja como se você fosse um DevOps Engeneer na empresa de tecnologia AUDAZ TECNOLOGIA. Gere um documento técnico as-built de uma infraestrutura de nuvem Oracle Cloud e AWS para o cliente TEN MEETINGS.
O nome da aplicação hospedada é 'Assembléia Digital'
Abaixo estão os componentes de infraestrura Cloud Native que são usados ​​pelo cliente:

Servidores virtuais Ubuntu e equipados com 2 vCPUs, 8 GB de RAM e 50 GB de armazenamento SSD na Oracle Cloud
Load balancers na Oracle Cloud
OKE na Oracle Cloud. O cluster OKE é configurado com três nós, cada um com 3 vCPUs, 16 GB de RAM e 150 GB de armazenamento SSD.
Postgres na Oracle Cloud
Redis cache no Kubernetes
Subnetes na Oracle Cloud
WAF na Oracle Cloud
Oracle Objecto Storage na Oracle Cloud
AWS S3
AWS Cloudfront
ElasticSearch for logging
ElasticSerch APM no Kubernetes
Fluentd no Kubernetes
Prometheus no Kubernetes
Grafana no Kubernetes
OpenVPN na Oracle Cloud


- Mantenha o comprimento total do documento em menos de 3500 palavras.
- Use o texto em terceira pessoa para todo o texto.
    """



structure="""
- Estrutura do AS-BUILT em 7 seções com títulos de markdown conforme mencionado:
 - ## Introduction:
 - ## Containers:
 - ## Bancos de dados:
 - ## Sites estáticos:
 - ## Rede:
 - ## VPNs:
 - ## Segurança:
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
        # modelId="amazon.titan-text-premier-v1:0",
        modelId="meta.llama3-8b-instruct-v1:0", # Meta llm (Facebook)
        messages=conversation,
        inferenceConfig={"maxTokens":2048,"stopSequences":[],"temperature":0.7,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
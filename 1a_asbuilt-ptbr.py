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


user_message = """Aja como se você fosse um DevOps Engeneer na empresa de tecnologia da empresa AUDAZ TECNOLOGIA. Gere um documento técnico as-built de uma infraestrutura de nuvem Azure para o cliente ETRO CONSTRUCTION.
O nome da aplicação hospedada é Siteblitz
Abaixo estão os componentes de infraestrura Cloud Native que são usados ​​pelo cliente:

- Object Storage	
- Sitebliz Backend	
- Virtual machines	
- Dados	
- SQL databases	
- Kubernetes (k3s)	
- Pods	
- Service	
- Ingress	
- Rede	
- DNS Zone	
- Rede Virtual	
- Virtual network gateway	
- Local network gateway	
- Load balancing (Application Gateway)
- Segurança
- WAF	
- Container registry
- Gateway de VPN
- VPN Site-to-site (IPsec). ETRO CONSTRUCTION com METATRON
- VPN Site-to-site (IPsec). ETRO CONSTRUCTION com AUDAZ TECNOLOGIA
- VPN Site-to-site (IPsec). Etro Produção com METATRON	
- VPN com SophosFW
- OpenVPN	para usuários remotos



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
        modelId="amazon.titan-text-premier-v1:0",
        messages=conversation,
        inferenceConfig={"maxTokens":3000,"stopSequences":[],"temperature":0.7,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
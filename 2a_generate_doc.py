# -*- coding: utf-8 -*-
# Use the Converse API to send a text message to Titan Text G1 - Premier.

import boto3
from botocore.exceptions import ClientError

dbg=0
boto3.setup_default_session(profile_name='audaz')


# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

user_message_en  = """Take the following considerations into account:
- Convert lines that start with numbers to titles and then use method add_heading
- Include all content from all sections in the script
- Use Arial font, without bold, size 10 and black for paragraphs
- Use Arial font, in bold, size 14 and black for titles and subtitles
- Include this command at the beginning of the script: from docx.shared import Pt
- Include this other command at the beginning of the script from docx.shared import RGBColor;

Generate a source code in python that uses the python-docx library to generate a word document with the content below:

"""
#  - crie um methodo add_content_ia e coloque todos os títulos e parágrafos dentro dele
#  - Converta a lista numerada do conteúdo para títulos


user_message  = """Leve em conta as seguintes considerações:
 - Desative a penalidade por repetição 
 - Inclua todo conteúdo de todas as seções no script
 - Inclua todas as seções no código
 - write every section
 - Não resuma
 - Use fonte Arial , sem negrito , tamanho 10 e cor preta para os parágrafos 
 - Use fonte Arial , em negrito, tamanho 14 e cor preta para os títulos e subtítulos 
 - Os títulos e subtítulos são criados usando o método `add_heading`. Não remova a numeração do título.
 - Os parágrafos são criados usando o método `add_paragraph`.
 - Inclua esse comando no ínicio do script: from docx.shared import Pt
 - Incluar este outro comando no ínicio do scripto from docx.shared import RGBColor; 

Gere um código fonte em python que utilize a biblioteca python-docx para gerar um documento word com o conteúdo abaixo:

"""

# with open("as-built-02.txt", "r") as file:
with open("as-built-02-ptbr.txt", "r") as file:
    # user_message += file.read().replace("\n", "")
    user_message += file.read()

if dbg>=1: print(user_message)


# Start a conversation with the user message.
user_message_example = """Leve em conta as seguintes considerações:
 - Desative a penalidade por repetição 
 - Crie um methodo add_content_ia e coloque todos os títulos e parágrafos dentro dele
 - Converta a lista numerada do conteúdo para títulos
 - Inclua todo conteúdo de todas as seções no script
 - Inclua todas as seções no código
 - write every section
 - Não resuma
 - crie um methodo add_content_ia e coloque todos os títulos e parágrafos dentro dele
 - Use fonte Arial , sem negrito , tamanho 10 e cor preta para os parágrafos 
 - Use fonte Arial , em negrito, tamanho 14 e cor preta para os títulos e subtítulos 
 - Os títulos e subtítulos são criados usando o método `add_heading`.
 - Os parágrafos são criados usando o método `add_paragraph`.
 - Inclua esse comando no ínicio do script: from docx.shared import Pt
 - Incluar este outro comando no ínicio do scripto from docx.shared import RGBColor; 

Gere um código fonte em python que utilize a biblioteca python-docx para gerar um documento word com o conteúdo abaixo:



As-built Document of XCorp's Cloud Infrastructure

This document provides an overview of XCorp's cloud infrastructure, which includes Kubernetes, KEDA, NGINX Ingress Controller, AWS CloudFront, AWS S3, AWS ECR, AWS Router53, Oracle Cloud Instance, RabbitMQ, Redis for caching, MySQL Heatwave, Postgres Database, ElasticSearch for logging and APM, and PRTG.

The following sections will cover the architecture, configuration, and deployment of these services, along with any best practices and recommendations for ongoing maintenance and optimization.

1. Architecture

XCorp's cloud infrastructure is designed to be highly available, scalable, and secure. The infrastructure is built on top of AWS and Oracle Cloud, with Kubernetes serving as the container orchestration platform.

1.1 Kubernetes

Kubernetes is used to manage and orchestrate containers across multiple nodes in the cluster. The cluster consists of multiple worker nodes, each running multiple pods, which are the smallest deployable units of computing in Kubernetes.

1.2 KEDA

KEDA (Kubernetes Event-driven Autoscaling) is used to automatically scale pods based on the number of events or messages received by the pod. This allows for fine-grained control over the scaling of applications and ensures that resources are used efficiently.

1.3 NGINX Ingress Controller

NGINX Ingress Controller is used to route traffic to the appropriate pods in the cluster. It acts as a reverse proxy and load balancer, ensuring that traffic is distributed evenly across the cluster.

1.4 AWS CloudFront

AWS CloudFront is used as a content delivery network (CDN) to cache static content and serve it to users from the nearest edge location. This helps to improve the performance of the application and reduce the load on the backend servers.

1.5 AWS S3

AWS S3 is used as a storage service for static content, such as images and videos. It provides high availability and durability, and can be used to store large amounts of data at a low cost.

1.6 AWS ECR

AWS ECR (Elastic Container Registry) is used as a container registry to store and manage container images. It provides secure and scalable storage for container images, and can be used to deploy containers to the cluster.

1.7 AWS Router53

AWS Router53 is used as a DNS service to route traffic to the appropriate IP address. It provides high availability and scalability, and can be used to manage DNS records for the application.

1.8 Oracle Cloud Instance

Oracle Cloud Instance is used as a compute service to run the application. It provides high performance and scalability, and can be used to run workloads that require a high degree of isolation and control.

1.9 RabbitMQ

RabbitMQ is used as a message broker to enable communication between different components of the application. It provides reliable and scalable messaging, and can be used to implement a variety of messaging patterns.

1.10 Redis for caching

Redis is used as a caching service to improve the performance of the application. It provides high-speed data storage and retrieval, and can be used to cache frequently accessed data.

1.11 MySQL Heatwave

MySQL Heatwave is used as a database service to store and manage data. It provides high performance and scalability, and can be used to implement a variety of database patterns.

1.12 Postgres Database

Postgres is used as a database service to store and manage data. It provides high performance and scalability, and can be used to implement a variety of database patterns.

1.13 ElasticSearch for logging and APM

ElasticSearch is used as a logging and monitoring service to collect and analyze logs from the application. It provides real-time search and analytics capabilities, and can be used to implement a variety of monitoring and alerting patterns.

1.14 PRTG

PRTG is used as a monitoring tool to monitor the health and performance of the infrastructure. It provides real-time monitoring and alerting capabilities, and can be used to implement a variety of monitoring and alerting patterns.

2. Configuration

The configuration of the infrastructure is managed using Terraform, an infrastructure as code (IaC) tool. Terraform provides a declarative language for defining the infrastructure, and allows for the creation, modification, and deletion of resources in a repeatable and consistent manner.

The Terraform configuration files are organized into modules, which represent reusable components of the infrastructure. 



"""




conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]


try:
    # Send the message to the model, using a basic inference configuration.
        # modelId="meta.llama2-70b-chat-v1",
    response = client.converse(
        modelId="meta.llama3-8b-instruct-v1:0",
        # modelId="amazon.titan-text-premier-v1:0",
        messages=conversation,
        inferenceConfig={"maxTokens":2048,"stopSequences":[],"temperature":0.7,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)
    if dbg>1: print(response)

except (Exception) as e:
    print(f"ERROR: Can't invoke . Reason: {e}")
    # print("ERROR: Can't invoke . Reason:")
    # print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

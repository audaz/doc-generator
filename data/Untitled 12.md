






Namespace(file='Untitled 12', a=None, b='value_2')






Namespace(file='Untitled 12', a=None, b='value_2')






Namespace(file='Untitled 12', a=None, b='value_2')









\generating file C:\Dev\doc-generator\data\metatron_manual\manual.docx...

1. Criar um Container Registry no Azure





- Acessar o Portal do Azure:

	- Entre no portal do Azure (https://portal.azure.com).

- Navegar at� Container Registries:

	- No menu lateral, clique em "Container registries" ou use a barra de pesquisa para encontrar.

- Criar um Novo Registro de Cont�iner:

	- Clique em "+ Add" no topo da p�gina para iniciar o processo de cria��o.

	- Preencha os campos obrigat�rios:

		- Subscription: Selecione a assinatura do Azure onde o registro ser� criado.

		- Resource Group: Escolha um grupo de recursos existente ou crie um novo.

		- Registry Name: D� um nome �nico ao seu registro de cont�iner.

		- Location: Escolha a regi�o onde o registro ser� criado.

		- SKU: Escolha entre Basic, Standard ou Premium, dependendo das suas necessidades.

	- Clique em "Review + Create" e depois em "Create" para concluir a cria��o.



![manual_1-1.png](manual_1-1.png)
IMG: manual_1-1.png



Link da documenta��o Azure 

https://learn.microsoft.com/pt-br/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli





2. Crie um Self-Hosted Agent no Azure DevOps



- Um Self-Hosted Agent � uma m�quina que voc� configura para ser usada como agente de build e deploy no Azure DevOps, ao inv�s de utilizar os agentes hospedados pela Microsoft. Isso permite maior controle sobre o ambiente de execu��o.

- Preparar a M�quina para o Self-Hosted Agent

- Escolher o Sistema Operacional:

	- O Self-Hosted Agent pode ser configurado em Windows, Linux ou macOS. Certifique-se de que a m�quina selecionada atende aos requisitos de sistema.

- Registrar o Self-Hosted Agent no Azure DevOps

- Acessar o Projeto no Azure DevOps:

	- No portal do Azure DevOps, navegue at� o projeto onde deseja configurar o agente.

- Ir para as Configura��es do Projeto:

	- No menu lateral, clique em "Project settings" (Configura��es do Projeto).

- Acessar a Se��o de Agentes:

	- Em Pipelines, clique em "Agent pools" (Pools de Agentes).

	- Selecione "Default" ou crie um novo Pool de Agentes se desejar separar os agentes.

- Adicionar um Novo Agente:

	- Clique em "New agent" para iniciar o processo de configura��o.

	- Escolha o sistema operacional da m�quina onde o agente ser� configurado.

-  Baixar e Configurar o Agente

  

- Baixar o Agente:

	- Siga as instru��es na tela para baixar o pacote do agente apropriado para o sistema operacional escolhido.

- Configurar o Agente:

	- Extraia o pacote do agente em um diret�rio apropriado.

	- No terminal ou prompt de comando, navegue at� o diret�rio do agente e execute o comando de configura��o fornecido na tela do Azure DevOps, que incluir� o URL do servidor do Azure DevOps e o token de autentica��o.

-            Verificar e Testar o Agente

- Verificar no Azure DevOps:

	- Ap�s configurar e iniciar o agente, volte ao portal do Azure DevOps e verifique se o agente aparece no pool de agentes com o status "Online".



Link da documenta��o Azure 

https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser#install





---
add page break

3. Criar uma Conex�o de Servi�o no Azure DevOps



- Acessar o Projeto no Azure DevOps:

	- Navegue at� o projeto onde deseja configurar a conex�o.

- Ir para Service Connections:

	- No menu lateral, selecione "Project settings" (Configura��es do Projeto).

	- Em Pipelines, clique em "Service connections".

- Adicionar uma Nova Conex�o de Servi�o:

	- Clique em "+ New service connection".

	- Selecione "Docker Registry" e clique em "Next".

- Configurar a Conex�o com o Container Registry:

	- No campo Docker Registry: insira o Login server do ACR (yourregistry.azurecr.io).

	- Em Docker ID e Docker Password: insira as credenciais de acesso ao ACR. Caso esteja usando um Service Principal, use o ID do Cliente e o Segredo do Cliente.

	- Em Service Connection Name: d� um nome amig�vel � conex�o, como my-acr-connection.

	- Selecione a op��o Grant access permission to all pipelines para facilitar o acesso ao registro em todos os pipelines do projeto.

	- Clique em Save para criar a conex�o.



Link da documenta��o Azure 

https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml



---
add page break

4. Criar Pipeline de Build e Deploy



Criar o Arquivo YAML:

- Na raiz do reposit�rio do seu projeto, crie um arquivo chamado azure-pipelines.yml.

- Abra o arquivo rec�m-criado e substitua o conte�do existente (se houver) pelo pipeline YAML fornecido abaixo. Certifique-se de salvar as altera��es.







```yaml
CODE DETECTED...
yaml

trigger:
inside_code

- workshop-node
inside_code

pool:
inside_code

  name: Azure Pipelines
inside_code

variables:
inside_code

- group: env_api_dev
inside_code

- name: dockerfilePath
inside_code

  value: '$(Build.SourcesDirectory)/Dockerfile'
inside_code

- name: tag
inside_code

  value: '$(Build.BuildId)'
inside_code

stages:
inside_code

- stage: Build_And_Push
inside_code

  jobs:
inside_code

  - job: BuildAndPushJob
inside_code

    pool: 'Azure Pipelines'
inside_code

    steps:
inside_code

    - checkout: self
inside_code

    - task: Docker@2
inside_code

      displayName: 'Login to Docker Registry'
inside_code

      inputs:
inside_code

        command: 'login'
inside_code

        containerRegistry: $(dockerRegistryServiceConnection)
inside_code

    - task: Docker@2
inside_code

      displayName: Build and push an image to container registry
inside_code

      inputs:
inside_code

        command: buildAndPush
inside_code

        repository: $(imageRepository)
inside_code

        dockerfile: $(dockerfilePath)
inside_code

        containerRegistry: $(dockerRegistryServiceConnection)
inside_code

        tags: |
inside_code

          $(tag)
inside_code

  
inside_code

  - job: DeployK8s
inside_code

    dependsOn: BuildAndPushJob
inside_code

    pool: $(agent-k8s)
inside_code

    steps:
inside_code

    - checkout: self
inside_code

  
inside_code

    - task: Bash@3
inside_code

      displayName: Check k8s
inside_code

      inputs:
inside_code

        targetType: 'inline'
inside_code

        script: | 
inside_code

          kubectl --kubeconfig=/home/azureuser/.kube/config get no,po,svc,ing -A 
inside_code

    - task: Bash@3
inside_code

      displayName: 'Deploy k8s'
inside_code

      env:
inside_code

        DOCKER_IMAGE: '$(containerRegistry)/$(imageRepository):$(tag)'
inside_code

        ENV: dev
inside_code

        NAME: '$(repository)'
inside_code

        PORT: $(port)
inside_code

        EMAIL: $(email)
inside_code

        CLIENTID: $(clientID)
inside_code

        SUBSCRIPTIONID: $(subscriptionID)
inside_code

        TENANTID: $(tenantID)
inside_code

        RESOURCEGROUPNAME: $(resourceGroupName)
inside_code

        HOSTEDZONENAME: $(hostedZoneName) 
inside_code

        ENVIRONMENT: $(environment)
inside_code

        NAMEDNS: $(nameDNS)
inside_code

        SECRET-ACCESS-KEY: $(secret-access-key)
inside_code

        DOCKERCONFIGJSON: $(dockerconfigjson)
inside_code

        DATABASE_PASSWORD: $(database_password) 
inside_code

      inputs:
inside_code

        targetType: 'inline'
inside_code

        script: |
inside_code

          cat $(Build.SourcesDirectory)/k8s/deploy-k8s.yml | envsubst > k8s/deploy_temp.yaml
inside_code

          cat k8s/deploy_temp.yaml
inside_code

          kubectl --kubeconfig=/home/azureuser/.kube/config apply -f $(Build.SourcesDirectory)/k8s/deploy_temp.yaml
inside_code

```
CODE DETECTED...

function generate_pygments...
HTML output generated and saved to 'output.html'
116,68
max:116,lines:68
Image generated and saved as 'output.png'





---
add page break

5. Crie um Grupo de Vari�veis



- No Azure DevOps, v� para Pipelines > Library.

- Clique em + Variable group.

- Nomeie o grupo como env_api_dev e adicione as vari�veis necess�rias.



![manual_1-2.png](manual_1-2.png)
IMG: manual_1-2.png



 ![manual_1-3.png](manual_1-3.png)
IMG: manual_1-3.png



Link da documenta��o Azure 

https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=azure-pipelines-ui

---
add page break

6. Configure as Vari�veis Necess�rias para a Funcionalidade do Ambiente



- Adicione as seguintes vari�veis ao grupo env_api_dev:

	- agent-k8s (nome do Self-Hosted Agent ) 

	- clientID (ID do cliente (client ID) da identidade atribu�da pelo usu�rio no Azure. Esta identidade precisa ter permiss�es para manipular registros DNS na sua zona DNS) 

	- containerRegistry (Login server do Container registry no Azure  )

	- dockerconfigjson (Username e password do Container registry convertido em Base64  )

	- dockerRegistryServiceConnection (nome do servi�o de conex�o com o Container registry )

	- email (e-mail que ser� associado aos certificados emitidos pelo Let's Encrypt) 

	- environment ( define o ambiente do Azure que est� sendo usado, que no caso � a nuvem p�blica do Azure )

	- hostedZoneName (� o nome da zona DNS no Azure que voc� est� usando para seu dom�nio.)

	- imageRepository ( nome do Repositorio no Container registry )

	- nameDNS (nome do registro DNS)

	- port (porta em que a aplica��o ser� executada)

	- repository (nome do reposit�rio)

	- resourceGroupName ( nome do grupo de recursos no Azure onde os seus recursos ) 

	- subscriptionID (� o ID da assinatura do Azure onde seus recursos est�o alocados )

	- tenantID (� um identificador �nico atribu�do a cada locat�rio (ou inquilino) no Azure Active Directory (Azure AD). Ele � usado para identificar o locat�rio ao qual uma assinatura do Azure est� associada.) 

-  Configure as Vari�veis Necess�rias do Projeto

  

- Certifique-se de que as vari�veis do projeto est�o configuradas corretamente no arquivo YAML.



7. Crie um Diret�rio na Raiz do Projeto Chamado k8s



- Na raiz do reposit�rio do projeto, crie um diret�rio chamado k8s.

- Dentro do diret�rio k8s, crie um arquivo chamado deploy-k8s.yml.

- insira o conte�do abaixo no arquivo deploy-k8s.yml.



```
CODE DETECTED...


apiVersion: v1
inside_code

kind: Namespace
inside_code

metadata:
inside_code

  name: $ENV
inside_code

---
inside_code

kind: Deployment
inside_code

apiVersion: apps/v1
inside_code

metadata:
inside_code

  name: $NAME-backend-$ENV
inside_code

  namespace: $ENV
inside_code

spec:
inside_code

  replicas: 1
inside_code

  selector:
inside_code

    matchLabels:
inside_code

      deploy: $NAME-backend-$ENV
inside_code

  strategy:
inside_code

    type: Recreate
inside_code

  template:
inside_code

    metadata:
inside_code

      labels:
inside_code

        deploy: $NAME-backend-$ENV
inside_code

        app.kubernetes.io/name: $NAME-backend-$ENV
inside_code

    spec:
inside_code

      imagePullSecrets:
inside_code

        - name: docker-registry-secret
inside_code

      containers:
inside_code

        - name: $NAME-backend-$ENV
inside_code

          image: $DOCKER_IMAGE
inside_code

          ports:
inside_code

            - containerPort: $PORT
inside_code

          resources:
inside_code

            requests:
inside_code

              cpu: "10m"
inside_code

              memory: "250Mi"
inside_code

            limits:
inside_code

              cpu: "1"
inside_code

              memory: "600Mi"
inside_code

          env:
inside_code

            - name: DATABASE_PASSWORD
inside_code

              value: $DATABASE_PASSWORD
inside_code

      restartPolicy: Always
inside_code

---
inside_code

kind: Secret
inside_code

type: kubernetes.io/dockerconfigjson
inside_code

apiVersion: v1
inside_code

metadata:
inside_code

  name: docker-registry-secret
inside_code

  namespace: $ENV
inside_code

  labels:
inside_code

    app: $NAME-backend-$ENV
inside_code

data:
inside_code

  .dockerconfigjson: $DOCKERCONFIGJSON
inside_code

---
inside_code

apiVersion: traefik.containo.us/v1alpha1
inside_code

kind: Middleware
inside_code

metadata:
inside_code

  name: redirect
inside_code

  namespace: $ENV
inside_code

spec:
inside_code

  redirectScheme:
inside_code

    scheme: https
inside_code

    permanent: true
inside_code

---
inside_code

apiVersion: v1
inside_code

kind: Service
inside_code

metadata:
inside_code

  name: $NAME-$ENV-service
inside_code

  namespace: $ENV
inside_code

spec:
inside_code

  selector:
inside_code

    app.kubernetes.io/name: $NAME-backend-$ENV
inside_code

  type: ClusterIP
inside_code

  ports:
inside_code

    - protocol: TCP
inside_code

      name: porta$PORT
inside_code

      port: $PORT
inside_code

      targetPort: $PORT
inside_code

---
inside_code

apiVersion: cert-manager.io/v1
inside_code

kind: ClusterIssuer
inside_code

metadata:
inside_code

  name: letsencrypt-$ENV
inside_code

  namespace: cert-manager
inside_code

spec:
inside_code

  acme:
inside_code

    email: $EMAIL
inside_code

    privateKeySecretRef:
inside_code

      name: letsencrypt-$ENV
inside_code

    server: https://acme-v02.api.letsencrypt.org/directory
inside_code

    solvers:
inside_code

    - dns01:
inside_code

        azureDNS:
inside_code

          clientID: $CLIENTID
inside_code

          clientSecretSecretRef: 
inside_code

            name: cert-manager-azure-secret-key-$ENV
inside_code

            key: secret-access-key
inside_code

          subscriptionID: $SUBSCRIPTIONID
inside_code

          tenantID: $TENANTID
inside_code

          resourceGroupName: $RESOURCEGROUPNAME
inside_code

          hostedZoneName: $HOSTEDZONENAME
inside_code

          environment: $ENVIRONMENT
inside_code

---
inside_code

apiVersion: networking.k8s.io/v1
inside_code

kind: Ingress
inside_code

metadata:
inside_code

  name: $NAME-$ENV-backend
inside_code

  namespace: $ENV
inside_code

  annotations:
inside_code

    kubernetes.io/ingress.class: traefik
inside_code

    cert-manager.io/cluster-issuer: letsencrypt-$ENV
inside_code

    traefik.ingress.kubernetes.io/router.middlewares: $ENV-redirect@kubernetescrd
inside_code

spec:
inside_code

  ingressClassName: traefik
inside_code

  rules:
inside_code

  - host: $NAMEDNS-$NAME-backend.etroconstruction.dev
inside_code

    http:
inside_code

      paths:
inside_code

        - pathType: Prefix
inside_code

          path: /
inside_code

          backend:
inside_code

            service:
inside_code

              name: $NAME-$ENV-service
inside_code

              port:
inside_code

                number: $PORT
inside_code

  tls:
inside_code

  - hosts:
inside_code

    - $NAMEDNS-$NAME-backend.etroconstruction.dev
inside_code

    secretName: ingress-$ENV-$NAME-backend-tls
inside_code

```
CODE DETECTED...

function generate_pygments...
HTML output generated and saved to 'output.html'
116,196
max:116,lines:196
Image generated and saved as 'output.png'
file_path: C:\Dev\doc-generator\data\metatron_manual\manual.docx
funcion update_toc - dispatch

open        C:\Dev\doc-generator\data\metatron_manual\manual.docx

toc count=1
update

close

quit

Namespace(file='Untitled 12', a=None, b='value_2')
4. Esteiras de integração e implantação contínua ( CI/CD )

Nulla lacus odio, bibendum sed ante eget, eleifend venenatis metus. Quisque suscipit ex vel urna laoreet, a pharetra ipsum viverra. Sed ac fermentum ex. Nunc ut urna tincidunt nulla lobortis ullamcorper. Praesent nec mollis purus, sit amet tempus nunc. Sed efficitur velit nec dolor rhoncus laoreet. Donec imperdiet scelerisque justo condimentum interdum. Donec mollis urna ac libero tincidunt tincidunt. Donec scelerisque sit amet purus vitae molestie. Maecenas fermentum nec dolor id efficitur.

4.1.1	Pipeline (CI/CD) Siteblitz-Backend 

Este pipeline visa automatizar a construção de uma imagem Docker e a implantação de uma aplicação em um ambiente de Kubernetes. 


Configuração Inicial: 

•	Trigger: O pipeline é acionado quando ocorrem alterações no branch "Test,Staging,Master". 

•	Pool de Agentes: Utiliza o pool padrão do Azure Pipelines. 

•	Grupo de Variáveis: Utiliza um grupo de variáveis, para definir variáveis de ambiente compartilhadas. 

•	Variáveis: Define variáveis de ambiente adicionais, como a configuração de build, diretório temporário para CLI do .NET, nome do branch e versão da image



4.1.2	Estágio de BuildAndPush Integração Contínua (CI) 
 
BuildAndPushJob: Este job realiza a construção da imagem Docker e a publicação no registro de contêineres. 


Passo do BuildAndPushJob: 

 

•	Checkout: Baixa o código fonte do repositório. 

•	Login to Docker Registry: Realiza o login no registro de contêineres e constrói a imagem Docker com base no Dockerfile. 

•	Build and Push Docker image: Realiza o push da imagem Docker para o registro de contêineres, utilizando uma tag baseada na versão da build. Esta ação utiliza um serviço de conexão previamente configurado no Azure Pipelines para autenticar e conectar-se ao registro de contêineres, garantindo o correto armazenamento da imagem no repositório.


 
4.1.3	Estágio de DeployK8SJob (Entrega Contínua - CD) 
 
DeployK8SJob: Este job implanta a imagem Docker no cluster Kubernetes. 
 
Passo do BuildAndPushJob: 
 
•	Dependência: Dependente do job BuildAndPushJob para garantir que a imagem esteja disponível. 
•	 Checkout: Baixa novamente o código fonte do repositório (pode ser desnecessário e poderia ser removido para otimização). 
•	Deploy k8s: Utiliza variáveis de ambiente para definir parâmetros de implantação e executa um script Bash para implantar a imagem no Kubernetes. 
•	Substituição de Variáveis: O script Bash substitui variáveis no arquivo de configuração do Kubernetes antes de aplicar a implantação. 
•	Comandos kubectl: Usa o kubectl para listar recursos do Kubernetes e aplicar a implantação. 

Observações: 

O pipeline segue o padrão CI/CD, onde a Integração Contínua (CI) é representada pela construção da imagem Docker e a Entrega Contínua (CD) é representada pela implantação no Kubernetes. 
A Integração Contínua garante que a imagem Docker seja construída e disponível sempre que houver uma alteração no código fonte, enquanto a Entrega Contínua garante que a nova versão da aplicação seja implantada automaticamente no Kubernetes. 
 



4.1.4	Pipeline (CI/CD) Siteblitz-Frontend 

Este pipeline é responsável por automatizar a construção e implantação de uma aplicação web. Ele utiliza o Azure Pipelines para realizar várias etapas, desde a instalação das dependências até o upload dos arquivos para o Azure Blob Storage e a invalidação do cache no Azure Front Door. 
Configuração Inicial 
•	Trigger: O pipeline é acionado quando ocorrem alterações no branch "Test,Staging,Master". 
•	Agent Pool: Utiliza a imagem de máquina virtual "windows-latest". 
•	Variáveis: Usa um grupo de variáveis para definir variáveis de ambiente compartilhadas. 




4.1.5	Estágio BuildAndDeploy 

Este estágio contém os jobs e as etapas necessárias para construir e implantar a aplicação web. 
Job BuildAndDeployjob: 
 
•	NodeTool: Instala o Node.js na versão especificada. 
•	Script Install Dependencies: Instala as dependências do projeto usando o Yarn. 
•	Script Build: Constrói a aplicação web usando o Yarn e define variáveis de ambiente necessárias para a construção. 
•	Clean Azure Blob Container: Limpa o conteúdo do contêiner de Blob no Azure Storage. 
•	Upload to Azure Blob: Faz o upload dos arquivos da aplicação web para o contêiner de Blob no Azure Storage. 
•	Invalidate Front Door: Invalida o cache no Azure Front Door para refletir as alterações feitas na aplicação. 


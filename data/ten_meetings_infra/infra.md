1. Assembleia Digital - Infraestrutura de Nuvem Oracle Cloud e AWS

2. Introdução

A AUDAZ TECNOLOGIA foi contratada para projetar e implementar a infraestrutura de nuvem para a aplicação "Assembleia Digital" do cliente TEN MEETINGS. A infraestrutura foi projetada para atender às necessidades específicas da aplicação, garantindo alta disponibilidade, escalabilidade e segurança.

3. Oracle Cloud

A infraestrutura Oracle Cloud inclui os seguintes componentes:

* Servidores Virtuais: 5 servidores virtuais Ubuntu, equipados com 2 vCPUs, 8 GB de RAM e 50 GB de armazenamento SSD.
* Load Balancers: 2 Load Balancers na Oracle Cloud, configurados para balancear o tráfego de rede entre os servidores virtuais.
* OKE (Oracle Kubernetes Engine): um cluster OKE com 3 nós, cada um com 3 vCPUs, 16 GB de RAM e 150 GB de armazenamento SSD.
* Postgres: um banco de dados Postgres na Oracle Cloud, configurado para armazenar os dados da aplicação.
* Redis Cache: um cache Redis no Kubernetes, configurado para armazenar dados em cache.
* Subnetes: 3 subnetes na Oracle Cloud, configuradas para isolamento e segregação de redes.
* WAF (Web Application Firewall): um WAF na Oracle Cloud, configurado para proteger a aplicação contra ataques mal-intencionados.
* Oracle Object Storage: um armazenamento de objetos na Oracle Cloud, configurado para armazenar arquivos e dados.
* OpenVPN: um servidor OpenVPN na Oracle Cloud, configurado para fornecer acesso seguro à aplicação.

4. AWS

A infraestrutura AWS inclui os seguintes componentes:

* AWS S3: um bucket S3 para armazenamento de arquivos e dados.
* AWS Cloudfront: um distribuidor de conteúdo Cloudfront, configurado para distribuir conteúdo estático.
* ElasticSearch: um cluster ElasticSearch para logging e monitoramento.
* ElasticSerch APM: um sistema de monitoramento de aplicação ElasticSerch, configurado para monitorar o desempenho da aplicação.
* Fluentd: um sistema de coleta de logs Fluentd, configurado para coletar logs da aplicação.
* Prometheus: um sistema de monitoramento Prometheus, configurado para monitorar o desempenho da aplicação.
* Grafana: um sistema de visualização de dados Grafana, configurado para visualizar métricas da aplicação.

5. Conectividade e Segurança

A infraestrutura foi projetada para garantir alta disponibilidade e segurança. A conectividade entre os componentes foi estabelecida utilizando protocolos seguros, como SSL/TLS. Além disso, foram implementados mecanismos de autenticação e autorização para garantir que apenas usuários autorizados tenham acesso à aplicação.

7. Conclusão

A infraestrutura de nuvem Oracle Cloud e AWS para a aplicação "Assembleia Digital" do cliente TEN MEETINGS foi projetada e implementada com sucesso. A infraestrutura foi projetada para atender às necessidades específicas da aplicação, garantindo alta disponibilidade, escalabilidade e segurança.
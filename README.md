# doc-generator
Rotinas de automação de geração de documentos com uso de bibliotecas python e IA.

### TODO
+ Fazer parse de tabelas -  | nome [size=1] | tipo [size=1]| quantidade [size=1]| valor [size=1] |
- Criar alternativa de marcação para listas númeradas
- Variavel para data dinamica
- Criar um pipeline github actions para gerar documentos a cada commit na master
+++ Tratar abertura de arquivos com espaços para facilitar Obsidian

- Tratar imagens começando com [[
- Automatizar como remover tags do OKIT em .md ou fazer um parse para o JSON do OKIT.
- Pesquisar ferramentas de exportação para Azure e AWS.
- Criar opção de idioma váriavel




# Dicas
- Use --- como separador de páginas
- Começe uma linha com # , ## , ### para definir títulos (Assim como no formato markdown)
- Começe uma linha com 1. , 1.1 , 1.1.1 ou 1.1.1.1 para definir títulos númerados (No formato markdown seriam listas)
- Crie um arquivo logo.png na pasta do documento para que seja incluído na capa dinamicamente
- Tabela em centimetros
| nome [size=15] | tipo [size=1]| quantidade  valor [size=1] |


Assim como no formato MD (Markdown):
- Começe uma linha com - para difinir listas
- Use <!-- --> para envolver uma linha e ela não será exibida




### Idéias
- Ler pasta do Evernote e importar documentos e imagens
- Padronizar estrutura de diretórios para compatibilizar com o Vault do Obsidian
- Multi tenancy (multi empresas)



DONE
- Titulo variavel
- Logo dinamico por documento
- ToC opcional
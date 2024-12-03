# LacIA Vision LLM

LacIA Vision LLM é uma aplicação de inteligência artificial avançada desenvolvida pela Teledoc Journey Medical e Universidade Católica de Pelotas (UCPel), focada na avaliação de competências médicas através da análise de vídeos de procedimentos médicos.

## Descrição do Projeto

Este projeto utiliza tecnologias de ponta em IA, incluindo o Google Generative AI, para analisar vídeos de procedimentos médicos realizados por estudantes. A aplicação fornece avaliações detalhadas e feedback construtivo, auxiliando no processo de aprendizagem e avaliação de competências médicas.

### Principais Funcionalidades

- Upload de vídeos de procedimentos médicos
- Análise automatizada usando IA generativa
- Geração de avaliações somativas baseadas em checklists predefinidos
- Feedback detalhado e personalizado para estudantes
- Sugestões de leitura para aprimoramento de habilidades

## Tecnologias Utilizadas

- Python 3.9+
- Streamlit para interface do usuário
- Google Generative AI para análise de vídeo e geração de feedback
- Docker para containerização
- Git para controle de versão

## Requisitos de Sistema

- Python 3.9 ou superior
- Docker
- Conta no Google Cloud com acesso à API do Generative AI

## Configuração do Ambiente de Desenvolvimento

1. Clone o repositório:

   git clone https://github.com/jonasspezia/laciavisionllmv1.git
   cd laciavisionllmv1


2. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API do Google:

   GOOGLE_API_KEY=sua_chave_api_aqui


3. Crie e ative um ambiente virtual:

   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate


4. Instale as dependências:

   pip install -r requirements.txt


5. Execute a aplicação localmente:

   streamlit run main.py


## Uso do Docker

Para construir e executar a aplicação usando Docker:

1. Construa a imagem Docker:

   docker build -t teledocjourneymedical/laciavisionllmv1:latest .


2. Execute o container:

   docker run -p 8501:8501 --env-file .env teledocjourneymedical/laciavisionllmv1:latest


A aplicação estará disponível em `http://localhost:8501`.

## Sistema de Versionamento

O projeto utiliza um sistema de versionamento semântico. Para atualizar a versão:

1. Execute o script de atualização de versão:

   ./update_version.sh


2. Siga as instruções para inserir a nova versão.

3. O script atualizará o arquivo `version.txt`, criará uma tag Git e atualizará a imagem Docker automaticamente.

## Estrutura do Projeto

- `main.py`: Arquivo principal da aplicação Streamlit.
- `Dockerfile`: Instruções para construir a imagem Docker.
- `docker-compose.yml`: Configuração para implantação em ambientes de produção.
- `requirements.txt`: Lista de dependências Python.
- `.env`: Arquivo para armazenar variáveis de ambiente (não versionado).
- `.gitignore`: Lista de arquivos e diretórios ignorados pelo Git.
- `version.txt`: Arquivo contendo a versão atual do projeto.
- `update_version.sh`: Script para atualização de versão e implantação.

## Implantação

O projeto está configurado para implantação em um ambiente Portainer Swarm. Para implantar:

1. Certifique-se de que o Portainer está configurado com acesso ao seu repositório GitHub.
2. No Portainer, vá para "Stacks" e clique em "Add stack".
3. Escolha "Git repository" como método de implantação.
4. Insira a URL do repositório e as credenciais, se necessário.
5. Defina a variável de ambiente `GOOGLE_API_KEY` com sua chave API.
6. Implante a stack.

# Atualização do LacIA Vision LLM

## Desenvolvimento Local
a. Abra o projeto no VS Code.
b. Faça as alterações necessárias nos arquivos do projeto.
c. Teste as alterações localmente:

## Execute:
Para verificar se a aplicação funciona corretamente.

streamlit run main.py

## Controle de Versão
a. Abra um terminal no VS Code.
b. Verifique as alterações feitas:

git status

c. Adicione os arquivos alterados ao staging:

git add .

d. Faça o commit das alterações:

git commit -m "Descrição concisa das alterações"

## Atualização Automática de Versão
a. Execute o script de atualização de versão:

./update_version.sh

b. Quando solicitado, insira a nova versão (por exemplo, 1.0.1).
c. O script irá:

Atualizar o arquivo version.txt
Criar um novo commit com a versão atualizada
Criar uma nova tag do Git
Fazer push das alterações e da nova tag para o GitHub


## Construção e Teste da Imagem Docker
a. Construa a nova imagem Docker:

docker build -t teledocjourneymedical/laciavisionllmv1:latest .

b. Execute a imagem localmente para teste:

docker run -p 8501:8501 --env-file .env teledocjourneymedical/laciavisionllmv1:latest

c. Acesse http://localhost:8501 para verificar se a aplicação está funcionando corretamente.

## Push da Imagem Docker
a. Faça login no Docker Hub (se ainda não estiver logado):

docker login

b. Faça o push da nova imagem:

docker push teledocjourneymedical/laciavisionllmv1:latest

c. Faça o push da imagem com a tag da nova versão:

docker push teledocjourneymedical/laciavisionllmv1:v[nova_versão]

   Substitua [nova_versão] pela versão que você definiu no passo 3.


## Atualização da Implantação
a. Acesse o Portainer em portainer.laciavision.com.
b. Vá para "Stacks" e localize a stack do LacIA Vision LLM.
c. Clique em "Update stack".
d. Se necessário, atualize o docker-compose.yml para refletir a nova versão da imagem.
e. Clique em "Update" para aplicar as alterações.


## Verificação Pós-Implantação
a. Acesse a aplicação implantada (por exemplo, https://app.laciavision.com).
b. Verifique se as novas alterações estão funcionando corretamente.
c. Teste todas as funcionalidades principais para garantir que não houve regressões.

## Documentação e Comunicação
a. Atualize o README.md se houver mudanças significativas na funcionalidade ou no processo de instalação/uso.
b. Se aplicável, atualize a documentação do projeto.
c. Comunique as alterações à equipe e stakeholders relevantes.

## Monitoramento
a. Monitore os logs da aplicação após a implantação para identificar possíveis erros.
b. Verifique as métricas de desempenho para garantir que as alterações não impactaram negativamente o sistema.

## Rollback (se necessário)
a. Se problemas críticos forem detectados, considere reverter para a versão anterior:

No Portainer, selecione a versão anterior da imagem Docker.
Atualize a stack para usar a versão anterior.
b. Investigue e corrija os problemas antes de tentar uma nova implantação.

Seguindo este protocolo, você garante que todas as alterações sejam adequadamente versionadas, testadas e implantadas de forma consistente e segura. Isso ajuda a manter a integridade do software e facilita o rastreamento de mudanças ao longo do tempo.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia o arquivo CONTRIBUTING.md (a ser criado) para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## Licença

Este projeto está licenciado sob Licença Restrita - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Teledoc Journey Medical - Dr. Jonas Spezia - teledoc@teledocmedical.com

Link do Projeto: [https://github.com/jonasspezia/laciavisionllmv1](https://github.com/jonasspezia/laciavisionllmv1)

## Agradecimentos

- Universidade Católica de Pelotas (UCPel) pelo suporte e colaboração.
- Google Cloud pela provisão das APIs de IA generativa.

Este README fornece uma visão abrangente do projeto, incluindo:

Uma descrição detalhada do projeto e suas funcionalidades.
As tecnologias utilizadas e os requisitos do sistema.
Instruções passo a passo para configuração do ambiente de desenvolvimento.
Instruções para uso do Docker.
Explicação do sistema de versionamento implementado.
Detalhes sobre a estrutura do projeto.
Informações sobre implantação em ambiente de produção.
Seções sobre contribuições, licença e contato.
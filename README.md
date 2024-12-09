# Sistema de Gerenciamento de Investimentos

O **Sistema de Gerenciamento de Investimentos** é um projeto desenvolvido em Python para auxiliar na administração e análise de investimentos. O sistema permite que você acompanhe a performance de ações e fundos imobiliários, gerencie seu portfólio, e faça análises detalhadas com base nos dados coletados da bolsa B3 e de outras fontes financeiras.

## Funcionalidades

- **Monitoramento de Investimentos:** Acompanhe suas ações e fundos imobiliários, incluindo informações de cotação e movimentação financeira.
- **Análise de Dados:** Analise o desempenho dos seus investimentos com base em dados históricos e atuais.
- **Compra e Venda:** Execute operações de compra e venda de ativos diretamente no sistema.
- **Relatórios:** Gere relatórios e gráficos para uma visualização clara do seu portfólio.

## Requisitos

Certifique-se de que você tenha o Python instalado. Recomenda-se o Python 3.8 ou superior.

## Configuração do Ambiente Virtual

1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/usuario/nome-do-repositorio.git

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt

## Estrutura do Projeto
- main.py: Arquivo principal do projeto que executa o sistema.
- src/: Código fonte do projeto.
- data/: Pasta para dados (esta pasta é ignorada e não está incluída no repositório).
- reports/: Pasta para relatórios e arquivos do Power BI (a ser incluída futuramente).
- requirements.txt: Arquivo com as dependências do projeto.

## Uso
Para iniciar o sistema e começar a gerenciar seus investimentos, execute:

    python main.py

## Notas
- A pasta data e os arquivos de bases de dados foram ignorados e não estão incluídos neste repositório. Certifique-se de ter os dados necessários em seu ambiente local para o funcionamento completo do sistema.
- O arquivo do Power BI não está incluído no repositório, mas será adicionado futuramente. Você pode criar e adicionar seus próprios relatórios conforme necessário.

## Contribuição
Se você deseja contribuir com o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature ou correção:
    ```bash
    git checkout -b minha-nova-feature
3. Faça suas alterações e commit:
    ```bash
    git add .
    git commit -m "Adiciona nova feature"
4. Faça o push para o seu fork:
    ```bash
    git push origin minha-nova-feature

5. Abra um pull request no repositório original.

Todas as contribuições são bem-vindas!
# Data Pipeline: Crypto Price Tracker (ETL)
Este projeto demonstra a criação de um pipeline de dados básico seguindo os princípios de ETL (Extract, Transform, Load). O objetivo é capturar preços de criptomoedas em tempo real, processar os dados e armazená-los em um banco de dados relacional para futuras análises.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Bibliotecas de Dados: Pandas (Processamento e Transformação)

API: CoinGecko (Ingestão de dados em tempo real)

Banco de Dados: SQLite (Armazenamento local)

ORM/Conectores: SQLAlchemy (Interface com o banco de dados)

🏗️ Arquitetura do Pipeline
Extração (Extract): O script consome dados em formato JSON da API pública da CoinGecko, capturando o preço atual (USD) e o timestamp da última atualização para Bitcoin, Ethereum e Solana.

Transformação (Transform): * Conversão do formato JSON para um DataFrame Pandas.

Normalização da estrutura (Pivotagem das moedas de colunas para linhas).

Tratamento de tipos de dados (Conversão de Unix Timestamp para DateTime).

Adição de metadados (Data e hora do processamento).

Carga (Load): Os dados transformados são inseridos em uma tabela SQLite utilizando a estratégia de append, permitindo a construção de um histórico temporal de preços.

📊 Estrutura do Banco de Dados
A tabela precos_cripto possui a seguinte estrutura {Coluna}: [Descrição]:
{moeda}: [Nome da criptomoeda (Primary Key/String)], 
{preco_usd}: [Valor atual em dólar (Float)],
{timestamp_api}: [Data da última atualização fornecida pela API],
{data_processamento}: [Data e hora em que o pipeline foi executado]

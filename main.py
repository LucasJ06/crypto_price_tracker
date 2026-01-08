#%%
#importando as bibliotecas
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

#configuracoes
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_last_updated_at=true"
db_name = "sqlite:///crypto_data.db"

#extraindo o dado
def extrair_dados():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na API: {response.status_code}")
        return None

#transformando o dado
def tranformar_dados(dados_bruto):
    df = pd.DataFrame(dados_bruto).T
    df = df.reset_index()
    df.columns = ["moeda", "preco_usd", "last_update_at"]
    df["last_update_at"] = pd.to_datetime(df["last_update_at"], unit="s")
    df["data_extracao"] = datetime.now() #coluna para saber quando o script rodou
    return df


#carregando o dado para o banco
def carregar_dados(df):
    engine = create_engine(db_name)
    df.to_sql('precos_cripto', con=engine, if_exists='append', index=False)
    print("Dados persistidos com sucesso!")


#execução do script
if __name__ == "__main__":
    print("Iniciando Pipeline...")
    dados = extrair_dados()
    if dados:
        tabela = tranformar_dados(dados)
        carregar_dados(tabela)

        #validação e leitura do dados
        engine = create_engine(db_name)
        df_validacao = pd.read_sql("select * from precos_cripto", con=engine)
        print("Conteúdo atual do banco de dados: ")
        print(df_validacao.tail(6))



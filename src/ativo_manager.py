import yfinance as yf
import pandas as pd

class AtivoManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def _formatar_ticker(self, produto):
        """
        Formata o ticker adicionando o sufixo correto dependendo do tipo de ativo.
        Ações e BDRs normalmente têm o sufixo '.SA', e FIIs têm o sufixo '.SAF'.
        """
        produto = produto.strip().upper()
        
        if "11" in produto:  # FIIs geralmente têm '11' no ticker
            return f"{produto}.SA"
        else:
            return f"{produto}.SA"  # Ações e BDRs usam '.SA'
    
    def buscar_cotacao(self, ticker):
        """
        Busca a cotação atual do ativo usando yfinance.
        """
        try:
            ativo = yf.Ticker(ticker)
            cotacao_atual = ativo.history(period="1d")['Close'][0]
            return cotacao_atual
        except Exception as e:
            print(f"Erro ao buscar cotação para {ticker}: {e}")
            return None
    
    def atualizar_cotacoes(self):
        """
        Lê o arquivo de ativos processados, remove duplicatas, busca as cotações atuais
        e atualiza o arquivo CSV.
        """
        df = pd.read_csv(self.file_path)

        # Remove duplicatas baseando-se na coluna 'Produto'
        df_unique = df.drop_duplicates(subset=['Produto']).reset_index(drop=True)

        # Adiciona uma nova coluna para armazenar as cotações atuais
        df_unique['Cotação Atual'] = None

        for index, row in df_unique.iterrows():
            produto = row['Produto']
            ticker_formatado = self._formatar_ticker(produto)

            print(f"Buscando cotação para {produto} ({ticker_formatado})...")
            cotacao = self.buscar_cotacao(ticker_formatado)
            
            if cotacao:
                df_unique.at[index, 'Cotação Atual'] = cotacao
        
        # Atualiza o DataFrame original com as cotações atuais
        df = df.merge(df_unique[['Produto', 'Cotação Atual']], on='Produto', how='left')

        # Salva o DataFrame atualizado com as cotações no mesmo arquivo CSV
        df.to_csv(self.file_path, index=False)
        print(f"Cotações atualizadas e salvas em: {self.file_path}")

import pandas as pd
from src.integration_selenium import ChromeBrowser
# from integration_selenium import ChromeBrowser
class CSVManager:
    def __init__(self, file_path,profile_path):
        """
        Inicializa o manipulador do arquivo CSV.

        :param file_path: Caminho para o arquivo CSV de produtos.
        """
        self.file_path = file_path
        self.produtos = None
        self.profile_path = profile_path

    def load_data(self):
        """
        Carrega as informações do arquivo CSV de produtos usando pandas.
        """
        try:
            # Carrega os produtos
            self.produtos = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Erro ao processar o arquivo CSV: {e}")

    def process_produtos(self):
        """
        Processa os produtos e atualiza produtos com status em branco.
        """
        produtos_para_processar = []
        if self.produtos is not None:
            for index, produto in self.produtos.iterrows():
                if produto['Status'] != 'lancado':
                    data_iso = produto['Data']
                    # Separando e rearranjando os componentes da data
                    ano, mes, dia = data_iso.split('-')
                    data_brasileira = f"{dia}/{mes}/{ano}"

                    valor = str(produto['Valor da Operação']/produto['Quantidade']).replace(".", ",")
                    # Atualiza o status para "lançado"
                    produtos_para_processar.append({
                    'index': index,
                    'produto': produto['Produto'],  # Substitua pelo nome correto da coluna
                    'quantidade': int(produto['Quantidade']),  # Substitua pelo nome correto da coluna
                    'data':data_brasileira,
                    'Valor da Operação':valor
                    })
                    self.produtos.at[index, 'Status'] = 'lancado'
            # Salva as alterações no arquivo CSV de produtos

            browser = ChromeBrowser(self.profile_path)
            browser.start_browser()
            browser.navigate_to("https://www.google.com/finance/",produtos_para_processar)
            self._save_to_file()

    def _save_to_file(self):
        """
        Salva as alterações no arquivo CSV.
        """
        try:
            self.produtos.to_csv(self.file_path, index=False)
            print(f"Alterações salvas no arquivo {self.file_path}.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV: {e}")
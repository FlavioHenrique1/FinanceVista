import pandas as pd
from tkinter import filedialog
import os

class SpreadsheetCopier:
    def __init__(self, destino_path):
        self.destino_path = destino_path

    def selecionar_arquivo_origem(self):
        # Abrir uma caixa de diálogo para selecionar o arquivo de origem
        self.origem_path = filedialog.askopenfilename(filetypes=[("Arquivo Excel", "*.xlsx")])
        if not self.origem_path:
            print("Nenhum arquivo selecionado. O processo foi interrompido.")
            return False
        return True

    def copiar_dados(self):
        if not self.selecionar_arquivo_origem():
            return

        # Carregar a planilha de origem com pandas
        df_origem = pd.read_excel(self.origem_path)

        # Carregar a planilha de destino com pandas
        df_destino = pd.read_excel(self.destino_path)

        # Especificar o formato de data brasileiro
        date_format = "%d/%m/%Y"

        # Certificar-se de que as colunas 'Data' são do tipo datetime
        df_origem['Data'] = pd.to_datetime(df_origem['Data'], format=date_format, errors='coerce')
        df_destino['Data'] = pd.to_datetime(df_destino['Data'], format=date_format, errors='coerce')

        # Cria uma lista de datas existentes na coluna 'Data' da planilha de destino
        dates_in_destino = set(df_destino['Data'])

        # Filtrar as linhas da planilha de origem que não têm data correspondente na planilha de destino
        df_novas_linhas = df_origem[~df_origem['Data'].isin(dates_in_destino)]

        # Concatenar apenas as novas linhas na planilha de destino
        df_resultado = pd.concat([df_destino, df_novas_linhas], ignore_index=True)

        # Salvar a planilha de destino atualizada
        df_resultado.to_excel(self.destino_path, index=False)

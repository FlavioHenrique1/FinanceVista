import pandas as pd

class DataFetcher:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_excel(self.file_path)

    def filter_data(self, df, column_name, value):
        return df[df[column_name] == value]

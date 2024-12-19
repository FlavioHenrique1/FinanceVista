from src.data_processing import filter_dividends_and_interest, process_ativos
from src.ativo_manager import AtivoManager  # Importa a classe para buscar cotações
from src.Spreadsheet_copier import SpreadsheetCopier
from src.CSV_manager import CSVManager

def main():
    # Exemplo de uso:
    # caminho da planilha de destino (local fixo)
    input_path = 'data/b3_data.xlsx'
    copiar = SpreadsheetCopier(input_path)
    copiar.copiar_dados()

    
    # Caminhos para os arquivos CSV onde os dividendos e ativos serão salvos
    dividendos_output_path = 'data/dividendos_e_juros.csv'
    ativos_output_path = 'data/ativos_processados.csv'
    
    # Chama a função para processar dividendos e juros
    filter_dividends_and_interest(input_path, dividendos_output_path)
    
    # Chama a função para processar ativos
    process_ativos(input_path, ativos_output_path)
    
    # Após processar os ativos, atualiza as cotações
    print("Atualizando cotações dos ativos...")
    manager = AtivoManager(ativos_output_path)

    manager.atualizar_cotacoes()  # Atualiza as cotações no arquivo de ativos processados
    profile_path = r"C:\\Users\\fla-h\\AppData\\Local\\Google\\Chrome\\User Data"

    csv_manager = CSVManager(ativos_output_path,profile_path)
        
    # Carrega os dados
    csv_manager.load_data()
    # Processa os produtos
    csv_manager.process_produtos()

if __name__ == "__main__":
    main()

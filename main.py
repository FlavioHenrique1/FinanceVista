from src.data_processing import filter_dividends_and_interest, process_ativos
from src.ativo_manager import AtivoManager  # Importa a classe para buscar cotações

def main():
    input_path = 'data/b3_data.xlsx'
    
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

if __name__ == "__main__":
    main()

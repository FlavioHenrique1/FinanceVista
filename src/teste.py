import pandas as pd

def consolidar_compras(input_file_path, output_file_path):
    """Consolida as compras dos ativos processados e calcula o custo médio e valor total."""
    
    # Carrega o DataFrame com os dados processados
    df = pd.read_csv(input_file_path)
    
    # Verifica os nomes das colunas no DataFrame
    print("Nomes das colunas no DataFrame:")
    print(df.columns.tolist())
    
    # Filtra apenas as compras
    compras = df[df['Movimentação'] == 'Transferência - Liquidação']
    
    # Agrupa as compras por ativo
    compras_agrupadas = compras.groupby('Produto').agg({
        'Quantidade': 'sum',
        'Valor da Operação': 'sum'
    }).reset_index()
    
    # Calcula o custo médio
    compras_agrupadas['Custo Médio'] = compras_agrupadas['Valor da Operação'] / compras_agrupadas['Quantidade']
    
    # Renomeia as colunas para corresponder à saída desejada
    compras_agrupadas = compras_agrupadas.rename(columns={
        'Quantidade': 'Quantidade Total',
        'Valor da Operação': 'Valor Total da Compra'
    })
    
    # Salva o DataFrame consolidado em um arquivo CSV
    compras_agrupadas.to_csv(output_file_path, index=False)
    
    print(f"Compras consolidadas e salvas em: {output_file_path}")

# Caminho para o arquivo de entrada e saída
input_path = 'data/ativos_processados.csv'
output_path = 'data/compras_consolidadas.csv'

# Executa a função de consolidação
consolidar_compras(input_path, output_path)

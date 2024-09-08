import pandas as pd
import re

def filter_dividends_and_interest(input_file_path, output_file_path):
    """Filtra e salva os dividendos e juros sobre capital próprio em um arquivo CSV."""
    # Carrega os dados do arquivo Excel
    df = pd.read_excel(input_file_path)
    
    # Filtra as linhas onde a coluna 'Movimentação' é 'Dividendo' ou 'Juros Sobre Capital Próprio'
    filtro = df[df['Movimentação'].isin(['Dividendo', 'Juros Sobre Capital Próprio','Rendimento'])]
    
    # Salva o DataFrame filtrado em um arquivo CSV
    filtro.to_csv(output_file_path, index=False)
    
    print(f"Dividendos e Juros Sobre Capital Próprio salvos em: {output_file_path}")


def extract_action_code(produto):
    """Extrai o código da ação (parte antes do hífen)."""
    match = re.match(r'^([^-]+)', produto)
    if match:
        return match.group(1).strip().upper()
    return produto.strip().upper()

def process_ativos(input_file_path, output_file_path):
    """Processa as compras e vendas de ativos e salva o resultado em um arquivo CSV."""
    # Carrega os dados do arquivo Excel
    df = pd.read_excel(input_file_path)
    
    # Verifica os nomes das colunas
    print("Nomes das colunas no DataFrame:")
    print(df.columns.tolist())

    # Converte a coluna 'Data' para o tipo datetime
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

    # Extrai o código da ação (parte antes do hífen) para padronizar a comparação
    df['Produto'] = df['Produto'].apply(extract_action_code)

    # Filtra apenas as compras e vendas
    compras = df[
        (df['Entrada/Saída'] == 'Credito') & 
        (df['Movimentação'] == 'Transferência - Liquidação')
    ]
    vendas = df[
        (df['Entrada/Saída'] == 'Debito') & 
        (df['Movimentação'] == 'Transferência - Liquidação')
    ]
    
    # Ordena as compras e vendas por data
    compras = compras.sort_values(by='Data').reset_index(drop=True)
    vendas = vendas.sort_values(by='Data').reset_index(drop=True)

    # Lista para armazenar o resultado final
    resultado = []
    compras_excluidas = []

    print(f"Total de compras: {len(compras)}")
    print(f"Total de vendas: {len(vendas)}")

    # Processa cada venda
    for _, venda in vendas.iterrows():
        venda_data = venda['Data']
        venda_quantidade = venda['Quantidade']
        venda_produto = venda['Produto']
        
        print(f"Venda: {venda_produto} em {venda_data} - Quantidade: {venda_quantidade}")
        print("Filtrando compras anteriores à venda...")

        # Filtra as compras anteriores à venda para o mesmo produto
        compras_anteriores = compras[
            (compras['Data'] < venda_data) & (compras['Produto'] == venda_produto)
        ]
        
        print(f"Compras anteriores para {venda_produto} em {venda_data}:")
        print(compras_anteriores)
        
        if compras_anteriores.empty:
            print(f"Sem compras anteriores para a venda de {venda_produto} em {venda_data}")
            continue
        
        # Encontrar a compra mais próxima antes da data da venda
        compra_proxima = compras_anteriores.iloc[-1]
        
        compra_data = compra_proxima['Data']
        compra_quantidade = compra_proxima['Quantidade']
        
        print(f"Compra mais próxima para {venda_produto}:")
        print(compra_proxima)
        
        if compra_quantidade > venda_quantidade:
            # Se a quantidade da compra for maior que a da venda, reduz a quantidade da compra
            resultado.append({
                'Data': venda_data,
                'Produto': venda_produto,
                'Movimentação': 'Venda',
                'Quantidade': venda['Quantidade'],
                'Preço unitário': venda['Preço unitário'],
                'Valor da Operação': venda['Quantidade'] * venda['Preço unitário']
            })
            # Atualiza a quantidade da compra restante
            compras.loc[compras.index.get_loc(compra_proxima.name), 'Quantidade'] = compra_quantidade - venda_quantidade
            venda_quantidade = 0
        else:
            # Se a quantidade da compra for menor ou igual à da venda, elimina a compra
            resultado.append({
                'Data': venda_data,
                'Produto': venda_produto,
                'Movimentação': 'Venda',
                'Quantidade': compra_quantidade,
                'Preço unitário': compra_proxima['Preço unitário'],
                'Valor da Operação': compra_quantidade * compra_proxima['Preço unitário']
            })
            venda_quantidade -= compra_quantidade
            compras_excluidas.append(compra_proxima.name)
        
        # Remove a compra correspondente do DataFrame se o índice existir
        compras = compras[~compras.index.isin(compras_excluidas)]

    # Cria um DataFrame com o resultado final
    resultado_df = pd.DataFrame(compras)
    
    # Verifica o total de resultados e salva o DataFrame resultante em um arquivo CSV
    print(f"Total de resultados processados: {len(resultado_df)}")
    resultado_df.to_csv(output_file_path, index=False)
    
    print(f"Ativos processados e salvos em: {output_file_path}")

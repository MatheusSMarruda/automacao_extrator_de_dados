import pandas as pd
import os

coluna = input("Digite o nome da coluna a ser filtrada: ")

def filter_and_save_to_excel(input_csv, output_excel, chunk_size=500000, filter_column=coluna):
    # Solicita ao usuário os nomes das usinas a serem filtradas
    usinas = input("Digite os nomes das usinas separados por vírgula: ").split(",")
    usinas = [usina.strip() for usina in usinas]  # Remove espaços extras
 
    # Lista para armazenar os dados filtrados
    filtered_data = []
 
    # Lê o arquivo CSV em pedaços (chunks) com separador ";"
    reader = pd.read_csv(input_csv, chunksize=chunk_size, sep=';')
    
    for i, chunk in enumerate(reader):
        # Filtra as linhas onde a coluna contém os valores fornecidos
        filtered_chunk = chunk[chunk[filter_column].isin(usinas)]
        
        # Adiciona os dados filtrados à lista
        if not filtered_chunk.empty:
            filtered_data.append(filtered_chunk)
            print(f"Dados filtrados do chunk {i+1} adicionados com sucesso!")
 
    # Combina todos os pedaços filtrados em um único DataFrame
    if filtered_data:
        combined_data = pd.concat(filtered_data, ignore_index=True)
        # Ordena os dados pela coluna
        combined_data = combined_data.sort_values(by=filter_column)
        # Salva os dados combinados em uma única planilha no arquivo Excel
        combined_data.to_excel(output_excel, index=False, engine='openpyxl')
        print(f"Arquivo Excel '{output_excel}' gerado com sucesso com os dados filtrados!")
    else:
        print("Nenhum dado correspondente ao filtro foi encontrado.")
 
# Solicita ao usuário o caminho do arquivo CSV de entrada
input_csv = input("Digite o caminho completo do arquivo (COM nome e tipo de arquivo) CSV de entrada: ")

# Solicita ao usuário o diretório de saída e cria o caminho completo para o arquivo Excel
output_dir = input("Digite o diretório onde deseja salvar o arquivo Excel de saída (SEM nome e tipo de arquivo): ")
output_excel = os.path.join(output_dir, "dados_filtrados.xlsx")

# Executa a função
filter_and_save_to_excel(input_csv, output_excel)
# Importando as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os #bib para interagir com os arquivos do sistema
import sys #permite interagir com linhas de comando através de argumentos
# argv[0] é o nome do script, e os itens subsequentes (argv[1], argv[2], etc.) são os argumentos adicionais fornecidos.

sns.set()

# Função para plotar tabelas pivot e salvar os gráficos
def plota_pivot_table(df, value, index, func, ylabel, xlabel, diretorio_salvamento, nome_arquivo, opcao='nada'):
    if opcao == 'nada':
        pivot = pd.pivot_table(df, values=value, index=index, aggfunc=func)
    elif opcao == 'sort':
        pivot = pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value)
    elif opcao == 'unstack':
        pivot = pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack()
    pivot.plot(figsize=(15, 5))
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.tight_layout()  # Para evitar cortes em labels
    #os.path.join função da biblioteca os para salvar o gráfico no caminho especificado (diretorio_salvamento)
    plt.savefig(os.path.join(diretorio_salvamento, nome_arquivo)) 
    
    plt.close()  # Fecha a figura atual

# Verifica se o mês foi passado como argumento
if len(sys.argv) < 2: #se tiver menos que 2 argumentos no caso [0] e [1]
    print("Por favor, passe o mês como argumento. Exemplo: JAN, FEV, etc.")
    sys.exit()

mes = sys.argv[1] #nome do segundo argumento - no caso, o mês: JAN, FEV, MAR e etc...
print(f'O nome do nosso script é: {sys.argv[0]}') #o Argumento [0] é nomeado automaticamento com o nome do script
print(f'Mês de referência é: {mes}')

# Lendo o arquivo CSV correspondente ao mês passado como argumento
sinasc = pd.read_csv(f'./input/SINASC_RO_2019_{mes}.csv') # sys.argv[1]

# Selecionando nome do arquivo a partir dos 7 primeiros caracteres da Data de Nascimento
max_data = sinasc.DTNASC.max()[:7] #o nome do arquivo salvo (os gráficos) será os 7 primeiros caracteres de DTNASC
print(max_data)

# Diretório de salvamento
diretorio_salvamento = f'C:/Users/giova/OneDrive/Área de Trabalho/EBAC Apostilas e Notebooks - Copia/Modulo 14/{max_data}'
os.makedirs(diretorio_salvamento, exist_ok=True) #os.makedirs: função da bib os para criar diretórios no sistema
#o metodo exist_ok=True garante que não haja erro caso o diretorio já existir

# Chamadas à função plota_pivot_table e salvamento dos gráficos
plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'Média Idade da Mãe', 'Data de Nascimento', diretorio_salvamento, 'media_idade_mae_por_data.png')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso Bebê', 'Escolaridade Mãe', diretorio_salvamento, 'peso_por_escolaridade_mae.png', 'sort')
plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'Média Idade Mãe', 'Data de Nascimento', diretorio_salvamento, 'media_idade_mae_por_sexo.png', 'unstack')
plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'Média Peso Bebê', 'Data de Nascimento', diretorio_salvamento, 'media_peso_bebe_por_sexo.png', 'unstack')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso Mediano', 'Escolaridade Mãe', diretorio_salvamento, 'peso_mediano_por_escolaridade_mae.png', 'sort')
plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'APGAR1 Médio', 'Gestação', diretorio_salvamento, 'apgar1_medio_por_gestacao.png', 'sort')

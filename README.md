# Script de Análise de Dados do SINASC

Este repositório contém um script Python para análise de dados do Sistema de Informações sobre Nascidos Vivos (SINASC).
O script está salvo como um arquivo `.py` e é projetado para processar e visualizar dados de nascimentos registrados.

# Funcionalidades
- Importação de bibliotecas essenciais como `numpy`, `pandas`, `matplotlib`, e `seaborn`.
- Interatividade com o sistema de arquivos e a linha de comando para receber argumentos.
- Leitura de arquivos CSV específicos baseados nos argumentos passados (mês de referência).
- Criação de tabelas pivot para análise e visualização de diferentes métricas.
- Geração e salvamento automático de gráficos em um diretório especificado.

# Uso
Para executar o script, é necessário passar o mês de referência como argumento na linha de comando. 
Exemplo python nome_do_script.py JAN

# Argumentos
 - `sys.argv[1]`: Mês de referência para análise (ex.: JAN, FEV, MAR, etc.).

# Funções Principais
 plota_pivot_table
 Esta função gera tabelas pivot e salva os gráficos gerados. Os parâmetros incluem colunas do DataFrame para análise,
 rótulos dos eixos, diretório de salvamento, entre outros.

# Estrutura do Código
 O script inicia importando bibliotecas necessárias e define a função `plota_pivot_table` para a geração de gráficos.
 Posteriormente, verifica o argumento passado (mês) e lê o arquivo CSV correspondente. Em seguida, realiza diversas chamadas
 à função `plota_pivot_table` para gerar e salvar gráficos baseados nos dados.

# Salvamento de Gráficos
 Os gráficos são salvos em um diretório específico, criado automaticamente pelo script com base na data mais recente
 presente no conjunto de dados.

 Este script é uma ferramenta valiosa para a análise rápida e visualização de dados do SINASC, facilitando a compreensão
# de tendências e padrões em nascimentos registrados.

import pandas as pd
import os
import numpy as dsa

caminho_do_arquivo_csv = "dataset.csv"
dados = pd.read_csv(caminho_do_arquivo_csv, sep=',', encoding='utf-8')
#dados = dsa.load(caminho_do_arquivo_csv, encoding='utf-8' )

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#   print(dados)
# Carregando um dataset para dentro de um array
# DELIMITER = RETIRAR VIRGULA
# USECOLS = COLETAR DADOS SOMENTE DOS INDEXACAO OU COLUNA
# SKIPROWS = COMEÇAR A PARTIR DA INDEXACAO 1 DESCONSIDERAR CABESARIO

# Carregar os dados para um DataFrame usando pd.read_csv
# with pd.option_context(delimiter=',', usecols=(0, 1, 2, 3), skiprows=1)

# Exibir todas as linhas do DataFrame
# print(dados)

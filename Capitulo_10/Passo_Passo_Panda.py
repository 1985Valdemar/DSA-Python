# 1. Criando um DataFrame
# Começamos importando a biblioteca Pandas e criando um DataFrame chamado “dados” com três colunas: “Nome”, “Idade” e “Cidade”. Preenchemos com alguns dados.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Idade': [25, 30, 22, 35, 18],
        'Cidade': ['SP', 'RJ', 'SP', 'MG', 'RS']}

dados = pd.DataFrame(data)

# 2. Acessando Dados
# Aprendemos a acessar informações imprimindo as primeiras 5 linhas do nosso DataFrame “dados”.

primeiras_linhas = dados.head()
print(primeiras_linhas)

# 3. Filtrando Dados
# Criamos um novo DataFrame chamado “maiores_de_idade” que contém apenas as pessoas com idade maior ou igual a 18.

maiores_de_idade = dados[dados['Idade'] >= 18]


# 4. Ordenando Dados
# Ordenamos o DataFrame “dados” por idade em ordem decrescente.

dados_ordenados = dados.sort_values(by='Idade', ascending=False)


# 5. Agregação de Dados
# Calculamos a média de idade das pessoas no DataFrame “dados”.

media_idade = dados['Idade'].mean()

# 6. Adicionando uma Nova Coluna
# Expandimos nosso DataFrame adicionando uma coluna chamada “Estado” e preenchendo com valores fictícios.

dados['Estado'] = ['SP', 'RJ', 'MG', 'SP', 'RS']

# 7. Removendo Colunas
# Simplificamos o DataFrame removendo a coluna “Cidade”.

# dados = dados.drop(columns='Cidade')

# 8. Salvando e Carregando Dados
# Aprendemos a salvar o DataFrame “dados” em um arquivo CSV chamado “dados.csv” e depois carregá-lo de volta para um novo DataFrame chamado “dados_carregados”.

dados.to_csv('dados.csv', index=False)
dados_carregados = pd.read_csv('dados.csv')

# 9. Consultas Condicionais
# Selecionamos todas as pessoas no DataFrame “dados” que vivem em um estado específico, por exemplo, “SP”.

pessoas_SP = dados[dados['Estado'] == 'SP']

# 10. Contagem de Valores
# Contamos quantas pessoas no DataFrame “dados” têm a mesma idade.

contagem_idades = dados['Idade'].value_counts()

# 11. Substituição de Valores
# Substituímos todas as ocorrências do estado “SP” por “São Paulo” no DataFrame “dados”.

dados['Estado'].replace('SP', 'São Paulo', inplace=True)

# 12. Resumo Estatístico
# Geramos um resumo estatístico do DataFrame “dados” que inclui contagem, média, desvio padrão, mínimo e máximo das idades.

resumo_estatistico = dados.describe()

# 13. Preenchimento de Valores Ausentes
# Criamos um DataFrame com valores ausentes (NaN) e, em seguida, preenchemos esses valores com um valor padrão.


dados_ausentes = pd.DataFrame({'A': [1, 2, np.nan, 4],
                               'B': [np.nan, 2, 3, 4]})

dados_preenchidos = dados_ausentes.fillna(0)

# 14. Concatenação de DataFrames
# Criamos dois DataFrames e os concatenamos verticalmente.

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

concatenado = pd.concat([df1, df2], axis=0)

# 15. Mescle (Merge) de DataFrames
# Criamos dois DataFrames com uma coluna em comum e fizemos uma mesclagem (merge) baseada nessa coluna.

df1 = pd.DataFrame({'Chave': ['A', 'B'], 'Valor1': [1, 2]})
df2 = pd.DataFrame({'Chave': ['B', 'C'], 'Valor2': [3, 4]})

mesclado = pd.merge(df1, df2, on='Chave')

# 16. Agrupamento de Dados
# Agrupamos o DataFrame “dados” por estado e calculamos a média de idade em cada grupo.

agrupado = dados.groupby('Estado')['Idade'].mean()

# 17. Plotagem de Dados
# Visualizamos os dados criando um gráfico de barras que mostra a contagem de pessoas em cada estado no DataFrame “dados”.


contagem_por_estado = dados['Estado'].value_counts()
contagem_por_estado.plot(kind='bar')
plt.xlabel('Estado')
plt.ylabel('Contagem')
plt.show()

# 18. Filtros Avançados
# Usamos filtros avançados para selecionar pessoas com idade entre 25 e 35 anos e que vivem no “RJ”.

filtro_avancado = dados[(dados['Idade'] >= 25) & (
    dados['Idade'] <= 35) & (dados['Estado'] == 'RJ')]

# 19. Pivotagem de Dados
# Realizamos uma pivotagem de dados no DataFrame “dados” para criar uma nova tabela que mostra a média de idade por estado.

tabela_pivot = pd.pivot_table(
    dados, values='Idade', index='Estado', aggfunc='mean')

# 20. Exportação de Dados
# Por fim, exportamos o DataFrame “dados” para um arquivo Excel chamado “dados.xlsx”.

dados.to_excel('dados.xlsx', index=False)

# https://pandas.pydata.org/docs/

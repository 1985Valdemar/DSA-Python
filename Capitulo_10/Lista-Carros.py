import pandas as pd

#pd.__version__
#print(pd)

# CRIANDO DICIONARIO DE CARROS
dados = {'Carros':['Fusca','Pampa','Opala'],
         'Ano':[1970, 1987, 1976], 
         'Motor':[1300, 1.6, 4.4]  
}

# Imprimir dicionario
print(dados) 
 
# Convertendo para tabela
df = pd.DataFrame(dados)

# Visualizando em linhas e
df.head()
print(df)

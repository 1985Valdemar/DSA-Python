import pandas as pd

#pd.__version__
#print(pd)

# CRIANDO DICIONARIO DE CARROS
dados = {'ModelosCar':['Fusca','Pampa','Opala'],
         'Ano':[1970, 1987, 1976], 
         'Motor':[1300, 1.6, 4.4],
         'Cor':['Bege', 'Azul', 'Creme']           
}

# Imprimir dicionario
print("Primeiro Dicionário Com Panda")
print(dados) 

# Convertendo para tabela DF = dataFrame
df = pd.DataFrame(dados)

# Visualizando em linhas e
df.head()
print("\nPrimeira Tabela")
print(df)
 
# Criando nova DF para inserir indexacao e local
df2 = pd.DataFrame(dados,
                   columns=['ModelosCar','Ano', 'Motor', 'Cor'],
                   index=['Pai', 'Mãe', 'Filho'])

print("\nRenomeando Indexação")
print(df2)

# metodo inserir coluna com panda
Estad = ["Bom", "Ruim", "Top"]

df2.insert(4, "Estado", Estad)
print("\nAdicionando Coluna Estado")
print(df2,"\n")
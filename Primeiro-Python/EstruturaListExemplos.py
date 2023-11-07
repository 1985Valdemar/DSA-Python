# Criando uma Lista
# [] COLCHETE E LISTA
lista_numeros = [10, 20, 50, -3.4]

# Ler Lista COMPRIMENTO DA LISTA CHAVE E VALORES
quantidade = len(lista_numeros)
# Quantidade
maximo = max(lista_numeros)
# Minimo
minimo = min(lista_numeros)
print("Sua Lista tem Quantidade:", quantidade, ",",
      "Maior Numero:", maximo, ",", "Menor Numero:", minimo)

# append = adicionar
# count = pesquisar item
# a = [] lista fazia
# a.append(50) = lista adicionar numero
# extend = adicionar lista

a = []
a.append(50)
print(a)
a.append(50)
print(a)
quantidade1 = a.count(50)
print(quantidade1)

old_list = [1, 2, 5, 10]
new_list = []

# copiando os itens de uma lista para outra
# PARA CADA ITEM DA LISTA OLD ADICIONE A NEWLIST
for item in old_list:
    new_list.append(item)
    print(new_list)

cidades = ['Recife', 'Manaus', 'Salvador']
# extend = adicionar
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)

# Buscar Indice = index
#Indice começa em 0 ZEROOO
indice = cidades.index('Manaus')
print(indice)

#Inserir com Indicação Indice = cidades.insert(2=indice, 110 igual item para adicionar)
cidades.insert(2,110)
print(cidades)

#Remover item cidades.remove(110)
cidades.remove(110)
print(cidades)

#Reverter Lista = reverse
cidades.reverse()
print(cidades)

#Ordernar lista = sort
x = [6,5,4,3,2,1,0]
x.sort()
print(x)

y = []

#PARA ITENS DENTRO DE X FAÇA: LISTA Y.ADICIONA(ITEM) IRA GERAR UMA COPIA
for item in x:
    y.append(item)
    print(y)
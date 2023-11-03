#Criando uma Lista
lista_1 = ["Arroz", "Frango", "Tomate", "Leite"]
type(lista_1)
#Imprimindo a lista
print(lista_1)

lista_2 = [23, 100, "Cientista de Dados"]
type(lista_2)
print(lista_2)

#INDEXACAO
item1 = lista_2[0]
item2 = lista_2[2]
item3 = lista_2[1]
print(item1, item2, item3)

#INDEXACAO
lista_1[1] = "CHOCOLATE"
print(lista_1)

#DEL
del lista_1[3]
print(lista_1)

#Lista Dentro Lista
listas = [[1,2,3],[10, 15, 14], [10.1, 8.7, 2.3]]
print(listas)

#Atribuir um item da lista a uma variavel
#indexacao posicao ZERO[0]
a = listas[0]
print(a)
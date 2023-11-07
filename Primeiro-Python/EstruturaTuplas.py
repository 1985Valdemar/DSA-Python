# () parentes e tuplas
# ESTRUTURA IMUTAVEL NÃO PODE MODIFICAR
# USAR PARA PARAMETROS SEGURANÇA

tupla1 = ("Geografia", 23, "Elefante", 9.8, 'Python')
print(tupla1)

# PESQUISA DE INDEXAÇÃO
indexacao = tupla1.index('Elefante')
print(indexacao)

# CONVERTENDO TUPLA PARA LISTA PRA SALVAR ALTERARACAO
t2 = ('A', 'B', 'C')
tipo = type(t2)
print(tipo)
# convesao
lista_t2 = list(t2)
tipo2 = type(lista_t2)
print(tipo2)

# LISTA T2 imprimir
print(lista_t2)

# ADICIONAR A LISTA
lista_t2.append('D')
print(lista_t2)

# CONVERSÃO DE LISTA PARA TUPLA PRA SALVAR EM TUPLA
t2 = tuple(lista_t2)
tipo3 = type(lista_t2)
print(t2)
print(tipo3)

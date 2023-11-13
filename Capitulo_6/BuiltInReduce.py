# Funcao Reduce = Reduzir

# IMPORTAR REDUCE DA FUNCTOOLS
from functools import reduce

Lista = [47, 11, 42, 13]
# Funçao SOma


def soma(a, b):
    x = a + b
    return x


reduzir = reduce(soma, Lista)
print("Sua Soma de: 47 + 11 + 42 + 13 é =",  reduzir)

lt = [47, 11, 42, 13]

reduzir2 = reduce(lambda x, y: x+y, lt)
print("Sua Soma de: 47 + 11 + 42 + 13 é =", reduzir2)

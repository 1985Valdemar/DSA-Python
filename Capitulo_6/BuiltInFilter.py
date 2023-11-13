# Filter = filtrar projeto
# CRIANDO FUNÇÃO PARA VERIFICAR PAR OU IMPAR
def verificarPar(num):
    # SE NUM / 2 RESTO O ENTÃO:
    if num % 2 == 0:
        return True
    else:
        return False

veri = verificarPar(35)
veri2 = verificarPar(36)
print("\n35 é par = ", veri, ",", "36 é par =", veri2)

# FUNCAO ANONIMA LAMBDA
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
verificarparLambda = list(filter(lambda x: x % 2 == 0, lista))
print("\nSeus Numeros Par São: ", verificarparLambda)

# Criada funcao Impar


def verificarImpar(num):
    # SE NUM / 2 RESTO O ENTÃO:
    if num % 2 == 1:
        return True
    else:
        return False


veri3 = verificarImpar(35)
veri4 = verificarImpar(36)
print("\n35 é Impar = ", veri3, ",", "36 é Impar =", veri4)

# FUNCAO ANONIMA LAMBDA
verificarparLambda = list(filter(lambda x: x % 2 == 1, lista))
print("\nSeus Numeros Impar São: ", verificarparLambda)

#FILTRAR LISTA ACIMA DE 6 USANDO FUNCAO ANONIMA A LAMBDA
acima6 = list(filter(lambda num: num > 6, lista))
print("\nSua Lista Acima de 6 é: ",acima6)
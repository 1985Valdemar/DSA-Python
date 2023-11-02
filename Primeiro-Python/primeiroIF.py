#gera codigo python que crie uma lista com os numeros entre 1 e 100 e entao inprima os numeros
# pares mas, somente se o numero for divisivel por 4.

# Cria uma lista com os números de 1 a 100
# Numero variavel para guardar
# = atribuição 
# list(range) e o intervalo do conteudo no caso de 1 a 100 101 é exclusivo não entra na conta
numeros = list(range(1, 101))

# Filtra os números pares divisíveis por 4 e os imprime
# for = para 
# numero = cada
# in = dentro
# numeros = da lista numeros
# : faça
for numero in numeros:
# if = se
# numero for divisivel 2 = 0 AND = & divisivel 4 = 0 
# Os dois verdadeiros
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)
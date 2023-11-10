# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

from cmath import sqrt

print("******************* Calculadora em Python *******************")

print("Selecione o Número Da Operação Desejada")

print(" 1 - Soma")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")
print(" 5 - Potencia")
print(" 6 - Raiz Quadrada")

menuopcao = input("\n Qual Operação Deseja (1/2/3/4/5/6): ")

numero1 = float(input("Digite um Numero: "))
if menuopcao == "5" or menuopcao == "6":
    print("Numero 2 é zero")
numero2 = float(input("Digite um Numero: "))
if menuopcao == "1":
    print("\n")
    print("Seu Resultado é:", numero1, "+", numero2, "=",  numero1+numero2 )
    print("\n")
elif menuopcao == "2":
    print("\n")
    print("Seu Resultado é:", numero1, "-", numero2, "=", numero1-numero2)
    print("\n")
elif menuopcao == "3":
    print("\n")
    print("Seu Resultado é:", numero1, "*", numero2, "=",  numero1*numero2)
    print("\n")
elif menuopcao == "4":
    print("\n")
    print("Seu Resultado é:", numero1, "/", numero2, "=",  numero1/numero2)
    print("\n")
elif menuopcao == "5":
    print("\n")
    print("Seu Resultado é:", numero1, "**", numero2, "=",  numero1 ** 2)
    print("\n")
elif menuopcao == "6":
    print("\n")
    print("Seu Resultado é:", numero1, "√x", numero2, "=",  (sqrt(numero1)))
    print("\n")
else:
    print("Digite Novamente aconteceu Erro")

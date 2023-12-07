# digitar numero
numero = int(input("Digite um número: "))

# se numero > 0 & numeroResto/2 diferente de 1
if numero > 0 and numero % 2 != 1:
    print("O número é positivo")
else:
    print("O número é impar")
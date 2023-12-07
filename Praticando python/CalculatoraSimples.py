#Implemente uma calculadora simples que realiza operações de adição, subtração, multiplicação e divisão:
import sys

print("*************** Sejam Bem Vindo/a **********************")
print("+++++++++++++++ Calculadora Simples ++++++++++++++++++++")
print(" 1 - Soma")
print(" 2 - Subtrair")
numero1 = float(input("Digite 1° Numero: "))
numero2 = float(input("DIgite 2° Numero: "))


operacao = input("Selecionar (1/2): ")

soma = numero1 + numero2

subtrair = numero1 - numero2

if operacao == "1":
    print("Valor da Soma é: ", numero1, "+", numero2, "=", soma)
elif operacao == "2":
    print("Valor da Subtração é: ", numero1, "-", numero2, "=", subtrair)
else:
    print("Falha na Operação Tentar Novamente")
    
print("-------------- Obrigado por Utilizar ----------------")
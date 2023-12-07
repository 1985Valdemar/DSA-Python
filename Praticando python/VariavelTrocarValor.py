#Atribua valores a duas variáveis e troque os valores entre elas sem usar uma variável temporária.
import sys

a = 20
b = 10

a = a + b
b = a - b
a = a - b

print("Valor de a = ",a , "Valor anterior = ",b)

print("\nValor de b = ", b, "Valor anterior = ",a)
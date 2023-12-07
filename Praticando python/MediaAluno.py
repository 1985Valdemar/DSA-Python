#Escreva um programa que calcule a média de três notas.
import sys

Nota1 = float(input("Digite 1° Nota: "))
Nota2 = float(input("Digite 2° Nota: "))
Nota3 = float(input("Digite 3° Nota: "))

media = (Nota1 + Nota2 + Nota3)/3

if media >= 7:
    print("Parabens Passou", media)
elif media >=5:
    print("Esta de Recuperação", media)
else:
    print("Reprovado",media)
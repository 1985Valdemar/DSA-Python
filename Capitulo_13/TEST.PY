# This is Python 2
import sys

# Leitura do valor de N
N = int(input())

# Leitura da palavra W
palavra = input()

# Remover espaços à direita e à esquerda da palavra
palavra_formatada = palavra.strip()

# Imprimir a palavra formatada N vezes
for _ in range(N):
    print (palavra_formatada)
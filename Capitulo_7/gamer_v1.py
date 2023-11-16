# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name

# Função para limpar a tela a cada axecuçao


def limpa_tela():

    # Para windows
    # NT nome Windows interno

    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função Game


def game():

    # Chamar limpa tela
    limpa_tela()

    print("\nBem Vindo(a) ao Jogo Da Forca!")
    print("\nAdivinhe a Palavra Abaixo Lembrando são carros:\n")

    # Lista de Palavras para Jogo
    palavras = ['kombi', 'pampa', 'fusca', 'opala']

    # Escolher de Forma aleatoria com Random
    # choice = escolher
    palavra=random.choice(list(palavras))

    # Criar List Comprehension
    # Para colocar traço da letra
    # vai contar para colocar traço
    letras_descobertas = ['_' for letra in palavra]

    # Numeros de chances
    # Qual quantidade Maxima de letra da lista? no caso 5
    chances = 5

    # lista para letras erradas
    letras_erradas = []

    # Criar Loop para Repetir Jogo
    # # Loop Enquanto numero de chance for maior do que zero
    while chances > 0:

        # Join Juntar
        print(" ".join(letras_descobertas))
        print("\nChances Restantes: ", chances)
        print("\nLetras Erradas:", "".join(letras_erradas))

        # Tenttivas Realizadas
        # .lower converter para minusculo
        tentativa = input("\nDigite Uma Letra: ").lower()

        # Condicional como tentativa
        # Se tentativa dentro palavra entao:
        if tentativa in palavra:
            index = 0

            # Para letra dentro palavra entao:
            for letra in palavra:
                # Se tentativa = letra entao:
                if tentativa == letra:
                    letras_descobertas[index] = letra

                 # incrementar no indice somando
                index += 1
        else:  # Decrementando da chances
            chances -= 1
            letras_erradas.append(tentativa)

            # Condicional Pra Vencer
            # se _ não estiver Dentro letras descobertas então:
        if "_" not in letras_descobertas:
            print("\nVocê Venceu, a Palavra era: ", palavra)
            break

    # Condicional Fim Chances
    # Se tiver _ dentro letras Descobertas então:
    if "_" in letras_descobertas:
        print("\nVocê Perdeu Tente Novamente, a Palavra era: ", palavra)


# Bloco Main
# MODULO PYTHON
if __name__ == "__main__":
    game()
    print("\nParabéns. Você Está Aprendendo Programação em Python com DSA. :)\n")

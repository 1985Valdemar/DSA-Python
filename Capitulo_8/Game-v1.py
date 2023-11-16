# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
class limpa_tela:
     
     def limpa_tela(self):
          # Windows
          if name == 'nt':
               _ = system('cls')
 
          # Mac ou Linux
          else:
               _ = system('clear')

# CLASSE + METODO DESENHAR FORCA

class display_hangam():
     def display_hangan(self,chances,board):
          self.chances = chances
          self.board = board
          
           # Lista de estágios da forca
            
               # Board (tabuleiro)
          board = [ #estágio  0(final)
               '''
               >>>>>>>>>>Hangman<<<<<<<<<<
               
               +---+
               |   |
                   |
                   |
                   |
                   |
               =========
               ''',
                 #estágio 1 
               '''
               +---+
               |   |
               O   |
                   |
                   |
                   |
               =========
               ''', 
                 #estágio 2 
               '''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
               =========
               ''',
                 #estágio 3 
               '''
               +---+
                |   |
                O   |
               /|   |
                    |
                    |
               =========
               ''',
                 #estágio 4 
               '''
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
               =========
               ''',
                 #estágio 5
               '''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
               =========
               ''',
                 #estágio 6 
               '''

               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
               =========
               ''']


# Classe
class Hangman:
     def game(self, limpa_tela):
          self.limpa_tela = limpa_tela
          limpa_tela = "Limpar"
          print("Seja Bem Vindo Jogo Forca")
          print("Adivinhe a Palavra Abaixo")
     
     # Método Construtor
     def __init__(self):
          print("Construtor iniciado") 
                   
     def chance(self, tabuleiro, chances, letras_tentativas,lista_letras_palavras, palavras):
          self.lista_letras_palavras = lista_letras_palavras
          self.tabuleiro = tabuleiro
          self.chances = chances
          self.letras_tentativas =letras_tentativas
          self.palavras = palavras
          
          
          
          palavras = ['uno', 'corolla', 'civic', 'bmw']
          
          palavra=random.choice(list(palavras))
          
            # Lista  de letras  da palavra
          lista_letras_palavras = [letra for letra in palavra]
          
          
          
              # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
          tabuleiro = ["_"] * len("palavra")
          
          # Número de chances
          chances = 7
          
          # Lista para as letras digitadas
          letras_tentativas = []
          
          # Loop enquanto número de chances for maior do que zero
          while chances > 0:
               
               print("\nChances Restantes: ", chances)
               print(display_hangam(chances))
               print("Palavra: ", tabuleiro)
               print("\n")
               
               # Tentativa
               tentativa = input("\nDigite uma letra: ")
               
               # Condicional
               if tentativa in letras_tentativas:
                    print("                              Você já tentou essa letra. Escolha outra!")
                    continue
               
               # Condicional
               if tentativa in lista_letras_palavras:
                    
                    print("                               Você acertou a letra!")
                    
                    # Loop
                    for indice in range(len(lista_letras_palavras)):

                         # Condicional
                         if lista_letras_palavras[indice] == tentativa:
                              tabuleiro[indice] = tentativa
                    
                    # Se todos os espaços foram preenchidos, o jogo acabou
                    if "_" not in tabuleiro:
                         print("\n*********************** Você venceu! A palavra era: {}***********************".format(palavra))
                         break
               else:
                    print("                               Ops. Essa letra não está na palavra!")
                    # Decremento
                    chances -= 1
                    letras_tentativas.append(tentativa)
          
          
          # Condicional
          if "_" in tabuleiro:
               print("\n################ :( Você perdeu! A palavra era: {}. ################ :( ".format(palavra))


          # Bloco main
if __name__ == "__main__":
     Hangman()
     print("\n:)****************:) Parabéns. Você está aprendendo programação em Python com a DSA. :)****************:)\n")

                    
                    
                    
                    
                    
               
               # Método para verificar se o jogo terminou
                    
               # Método para verificar se o jogador venceu
                    
               # Método para não mostrar a letra no board
                    
               # Método para checar o status do game e imprimir o board na tela


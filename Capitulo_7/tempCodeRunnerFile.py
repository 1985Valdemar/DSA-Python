
# Função do jogo
def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(list(palavras))
    
    # Lista  de letras  da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
    
    # Número de chances
    chances = 6
    
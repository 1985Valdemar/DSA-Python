# Criando a classe Livro com parâmetros no método construtor
# Classe DINAMICA para varios livros
# COLOCA PARAMETROS PARA SER EXECUTADOS
class Livro():

    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")

    def imprime (self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" % (titulo, isbn))


# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)
print(f"\n Seu Livro", Livro2)

# Atributo do objeto
titulo = Livro2.titulo
print(f"\nSeu Titulo Livro:")


# Método do objeto Livro2
Livro2.imprime("O Poder do Hábito",77886611)
print(f"\nAqui", Livro2)


# Criando a classe
class Algoritmo():
    # METODO CONSTRUTOR = TIPO ALGORITOMO COMO ARGUMENTO
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")


# Criando um objeto a partir da classe
algo1 = Algoritmo(tipo_algo='Random Forest')
print("\nAlgo1 = ", algo1)

# Criando um objeto a partir da classe
algo2 = Algoritmo(tipo_algo='Deep Learning')
print("\nAlgo2 = ", algo2)

# Atributo da classe
tipo1 = algo1.tipo
print("\nTipo Algo1 = ", tipo1)


# Atributo da classe
tipo2 = algo2.tipo
print("\nTipo Algo2 = ", tipo2)



# Criando uma classe chamada Livro
# Primeira Letra Maiscula
class Livro():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__ construtor para iniciar
    # (self) é uma REFERENCIA a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        
        # Atributos são propriedades 
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("\nConstrutor chamado para criar um objeto desta classe.")
        
    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
                                 #%s = placeHouder    %d = placeHouder  == MARCA COMO TITULO E ISBN
         print("\nFoi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))
         
# Criando uma instância da classe Livro
# LIVRO1 OBJETO DO TIPO LIVRO
Livro1 = Livro()

# O objeto Livro1 é do tipo Livro
tipo = type(Livro1)
print("\nTipo: ",tipo)

# O atributo do objeto livro1
titulo = Livro1.titulo
print("\nTitulo: ",titulo)

# Método do objeto Livro1
Livro1.imprime()
         
         
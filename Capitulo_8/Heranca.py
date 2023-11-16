# Criando a classe Animal - Super-classe
# EXPECIFICACAO GERAL NA MAE
# CLASSE MAE
class Animal:
    
    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")
        
    def emitir_som(self):
        pass
    
# Criando a classe Cachorro - Sub-classe
# CLASSE FILHA DA CLASSE ANIMAL MAE
# ADICIONA SOMENTE O NECESSARIO CARACTERISTICA BASE ESTA MAE
# EXPECIFICACAO ESPECIFICA DO CACHORRO
class Cachorro(Animal):
    
    # METODO CONSTRUTOR CACHORRO
    def __init__(self):
        # CONSTRUTOR CLASSE MAE
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")
        
# Criando a classe Gato - Sub-classe
# CLASSE FILHA
# ADICIONA SOMENTE O NECESSARIO CARACTERISTICA BASE ESTA MAE
# EXPECIFICACAO ESPECIFICA DO GATO
class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")


# Criando um objeto (Instanciando a classe)
rex = Cachorro()

# Criando um objeto (Instanciando a classe)
zeze = Gato()

# OBJETO SOM
rex.emitir_som() 

zeze.emitir_som() 

# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()

# Executando o método da classe Animal (super-classe)
rex.comer()

# EXECUTA O METODO DA CLASSE GATO (SUB-CLASSE) FILHA
zeze.imprimir()

# Executando o método da classe Cachorro (sub-classe)
zeze.comer()


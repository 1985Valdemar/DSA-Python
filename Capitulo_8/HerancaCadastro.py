
# Importar a classe Carro do arquivo HerancaCarroFilho
from HerancaCarroFilho import Carro

# Definir a classe Cadastro que herda da classe Carro
class Cadastro(Carro):
    pass

# Criar uma lista para armazenar carros cadastrados
carros_cadastrados = []

# Criar instâncias da classe Cadastro e adicioná-las à lista
carro1 = Cadastro("Toyota", "Corolla", 2006, "Prata", 135)
carro2 = Cadastro("Fiat", "Uno", 2008, "Verde", 98)

# Adicionar carros à lista
carros_cadastrados.append(carro1)
carros_cadastrados.append(carro2)

# Imprimir a lista de carros cadastrados
for carro in carros_cadastrados:
    print(carro)
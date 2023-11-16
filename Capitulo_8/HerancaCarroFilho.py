# CRIAR CLASSE FILHA PARA HERDAR


from herancaveiculomae import *


class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, cor, potencia):
        Veiculo.__init__(self, marca, modelo, ano, cor)
        print("OBJETO CARRO")
        self.potencia = potencia
    
    def __str__(self):
        return f"{super().__str__()}, Potência : {self.potencia}"

carro1 = Carro("Toyota", "Corolla", 2006, "Prata", 135)
print(carro1)
  
 
# CRIAR CLASSE MAE OU SUPER-CLASSE

class Veiculo:

    # METODO CONSTRUTOR
    def __init__(self, marca, modelo, ano, cor):
        print("Carro Cadastrado")
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

   

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}"

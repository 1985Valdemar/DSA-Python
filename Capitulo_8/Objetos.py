# Criando uma lista
# instancia classe lista
lst_num = ["Data", "Science", "Academy", "Nota", 10, 10]

# A lista lst_num é um objeto, uma instância da classe lista em Python
tipo = type(lst_num)
print("\nTipo é:", tipo)

# OUTRO MODO IMPRIMIR TIPO
print("\nSegundo Modo Imprimir Tipo = ",type([]))

# Contar
# metodo e atributo
quantidade = lst_num.count(10)
print("\nLista Original = ",lst_num)
print("\nQuantidade item 10 é =",quantidade)

# Usamos a função type, para verificar o tipo de um objeto
# CLASSES BUIT-IN
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

# Criando uma classe
class Estudantes:
    # CONSTRUTOR INIT 
    # 3 ARGUMENTOS
    def __init__(self, nome, idade, nota):
        # ATRIBUTOS DESTA CLASSE
        # NOME PARAMETROS
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Bob", 12, 9.5)
print("\nEstudante1 = ",Estudante1.nome,",",Estudante1.idade,"Anos,","Sua Nota Foi:",Estudante1.nota)

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nome
print("\nNome = ",Estudante1.nome)

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.idade
print("\nIdade = ",Estudante1.idade)

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nota
print("\nNota = ",Estudante1.nota)

# Criando uma classe
class Funcionarios:
    # METODO CONSTRUTOR
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo)


# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")
Func1.listFunc()

print("**** Usando atributos *****")
# TEM ATRIBUTO?
nome = hasattr(Func1, "nome")
print(nome)
sal = hasattr(Func1, "salario")
print(sal)
# MANIPULEI SALARIO
alterar = setattr(Func1, "salario", 4500)
print(alterar)
# PERGUNTA SALARIO FUNCIONARIO1
sal2 = hasattr(Func1, "salario")
print(sal2)
# RETORNA SALARIO FUNC1
Retorna = getattr(Func1, "salario")
print(Retorna)
# DELETAR SALARIO FUNC1
deleta = delattr(Func1, "salario")
print(deleta)
# PERGUNTA SALARIO FUNC1 TEM?
sal3 = hasattr(Func1, "salario")
print(sal3)





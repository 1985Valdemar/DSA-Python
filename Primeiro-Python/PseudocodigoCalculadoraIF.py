#Passo Passo Psedocodigo

#Calculadora Simples 
#Inicio
# Exibir "Seja Bem Vindo Calculadora"
# Peça um Numero
# Armazene este Numero
# Peça qual função deseja - + * /
# Peça segundo numero
# Armazene segundo numero
# Realizar função
# Mostrar resultado
#Fim#
print("Seja Bem Vindo Calculadora Simples")
numero1 = float(input("Digite um Numero: "))
Operacao = str(input("Digita qual Operação deseja realizar +,-,*,/ "))
numero2 = float(input("Digite um Numero: "))
if Operacao == "+":
    print("Seu Resultado é:",numero1+numero2)
elif Operacao == "-":
    print("Seu Resultado é:",numero1-numero2)
elif Operacao == "*":
    print("Seu Resultado é:",numero1*numero2)
elif Operacao == "/":
    print("Seu Resultado é:",numero1/numero2)
else:
    print("Digite Novamente aconteceu Erro")

    



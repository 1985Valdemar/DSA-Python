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
print("Seja Bem Vindo Calculadora")
numero1 = float(input("Digite um Numero: "))
funcao = str(input("Digita qual Função deseja realizar +,-,*,/ "))
numero2 = float(input("Digite um Numero: "))
if funcao == "+":
    print("Seu Resultado é:",numero1+numero2)
elif funcao == "-":
    print("Seu Resultado é:",numero1-numero2)
elif funcao == "*":
    print("Seu Resultado é:",numero1*numero2)
elif funcao == "/":
    print("Seu Resultado é:",numero1/numero2)
else:
    print("Digite Novamente aconteceu Erro")

    



# TRATAMENTO ERROS TENTAR EVITAR ERROS
def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print("Você não digitou um número!")
            continue
        else:
            print("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print(val)

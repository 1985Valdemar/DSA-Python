#with open('arquivos/cientista.txt','r') as arquivo:
 #   conteudo = arquivo.read()
    
#print(len(conteudo))

#print(conteudo)


#with open('arquivos/cientista.txt','w') as arquivo:
    #arquivo.write(texto[:19])
    #arquivo.write('\n')
    #arquivo.write(texto[28:66])
    
# TRATAMENTO ERROS TENTAR EVITAR ERROS
def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val)
        
askint()
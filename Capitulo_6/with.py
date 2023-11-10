with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()
    
print(len(conteudo))

print(conteudo)


#with open('arquivos/cientista.txt','w') as arquivo:
    #arquivo.write(texto[:19])
    #arquivo.write('\n')
    #arquivo.write(texto[28:66])
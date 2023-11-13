# FUNCAO ENUMERATE = NUMERAR POR ONDEM
sequencia = ['a', 'b', 'c', 'd']
numerar = list(enumerate(sequencia))
print("\nSua Lista Sequencia Numerada: ", numerar,"Python Indexação Inicia do 0")

# CRIAR POR COLUNA
# PARA INDICE COLOCAR VALOR DENTRO DE ENUMERATE DA SEQUENCIA
for indice, valor in enumerate(sequencia):
    print("Sua coluna e está: ",indice, valor)
    
# PARA INDICE MAIOR IGUAL 2 DENTRO DO ENUMERATE DA SEQUENCIA
for indice, valor in enumerate(sequencia):
    # SE INDICE MAIR IGUAL2 FAÇA:
    if indice >= 2:
        # PARAR
        break
    else:
        print(valor)
    
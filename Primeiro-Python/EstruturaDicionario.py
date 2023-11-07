# Dicionario guarda valores para cunsulta GARANTE POIS SÃO INDEPENDENTE
# item e par de chave"" e : valor
# chave"pedro":valor24
# {} = CHAVE É O DICIONARIO

estudantes_dict = {"Pedro": 24, "Ana": 22, "Frank": 6}
print(estudantes_dict)

selecionar = estudantes_dict["Frank"]
print("Frank tem:", selecionar, "Anos")

# CRIAR NOVA CHAVE COM NOVO VALOR NO CASO MARCELO=23ANOS
estudantes_dict["MARCELO"] = 23
print(estudantes_dict)

# clear para limpar APAGAR TUDO dicionario
estudantes_dict.clear()
print(estudantes_dict)

# DEL DELETA DICIONARIO
# UPDATE ADICIONAR LISTA
estudantes2 = {"Val": 38, "Dani": 39, "João": 6}
print(estudantes2)


estudantes3 = {"JUJU": 25, "Carlo": 35}
print(estudantes3)

# update
estudantes3.update(estudantes2)
print(estudantes3)
print(estudantes2)


# LISTA DENTRO DICIONARIO
dict3 = {'chave1': 1230, 'chave2': [22, 453, 73.4], 'chave3': [
    'picanha', 'fraldinha', 'alcatra']}
print(dict3)

# DEIXAR TUDO EM MAISCULO NO [INDICE 0] NO CASO PICANHA
maisculo = dict3['chave3'][0].upper()
print(maisculo)

# OPERAÇAO MATEMATICA DIMINIUR 2
var1 = dict3["chave2"][0] - 2
print(var1)

# {} = CHAVE É O DICIONARIO
#UM DICIONARIO DENTRO OUTRO ANINHADO
dict_aninhado = {'key1': {'key2_aninhado': 123456}}
print(dict_aninhado)

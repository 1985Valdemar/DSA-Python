# Criação de função
def potencia(x):
    return x ** 2


numeros = [1, 2, 3, 4, 5]

# DECLARAR NUMEROS AO QUADRADO
numero_quadrado = list(map(potencia, numeros))
print("\nSua lista ", numeros, "ao quadrado é: ", numero_quadrado)


# Convertendo temperaturas PARA CELSIUS
temperatura = [0, 22.5, 40, 100]
celsius = list(map(lambda x: (5.0/9)*(x - 32), temperatura))
print("\nSuas Temperaruras Convertidas para Celsius é: ", celsius)

# Convertendo temperaturas PARA FAHRENHIT
temperatura = [0, 22.5, 40, 100]
fahrenhit = list(map(lambda x: (((9.0)/5) * x + 32), temperatura))
print("\nSuas Temperaruras Convertidas para Celsius é: ", fahrenhit)

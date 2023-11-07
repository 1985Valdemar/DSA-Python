# Claro, aqui está um exemplo de código Python que cria uma lista de números de 1 a 100 e,
# em seguida, imprime os números pares que são divisíveis por 4 usando list comprehension:

# Cria uma lista com os números de 1 a 100
numeros = list(range(1, 101))

# Usa list comprehension para selecionar os números pares divisíveis por 4
numeros_pares_divisiveis_por_4 = [
    num for num in numeros if num % 2 == 0 and num % 4 == 0]

# Imprime os números pares divisíveis por 4
print("Números pares divisíveis por 4:")
print(numeros_pares_divisiveis_por_4)

print("oi")

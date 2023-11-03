
# Bubble Sort e algoritimo de ordernação simples que funciona comparando cada elemento com 
# proximo
# 
#inicio

# Para cada elemento i no array de tamanho n
#  Para cada elemento j no array de tamanho n - j
#    Se elemento i for maior que elemnto j
#      Troque os elementos i e j
# Exiba o array ordernado

#fim#



lista = [6, 3, 12, 7, 1, 5, 10]

#Função DEF
def bubble_sort(arr):
    n = len(arr)
    
    #Para cada elemento i no array 1°LOOP
    for i in range(n):
        
        #Para cada elemento j no array 2°LOOP
        for j in range(0, n-i-1):
            
            #Para Elemento i for maior que elemento j
            if arr[j] > arr[j+1]:
                
                #Troque os elementos i e j:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(lista))

lista2 = [100, 80, 60, 10, 20, 30, 50, 40, 70, 90]

print(bubble_sort(lista2))

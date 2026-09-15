lista = [5, -3, 9, -8, 2, -1]
negativo = []
positivo = []
#lista vazia []

for indice in range(len(lista)):
    if lista[indice] < 0:
        negativo.append(lista[indice])
    else:
        positivo.append(lista[indice])
    
        
print(lista)
print(negativo)
print(positivo)
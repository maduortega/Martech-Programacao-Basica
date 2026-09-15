import random

# Programa para preencher uma lista com 10 números inteiros
# e colocar os números em ordem crescente

def ler_dados():
    for i in range(10):
        lista.append(random.randint(2, 40))

def imprimir():
    for i in range(len(lista)):
        print(lista[i], end=' ')

def ordenar():
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i +1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    
            
            

# Principal

lista = []
ler_dados()
print('Dados antes da ordenação')
imprimir()
ordenar()
print()
print('Dados ordenados')
imprimir()
lista = []
pares = []
impares = []

for contador in range(7):
    numero = int(input('Informe um número:'))
    lista.append(numero)
    
    if lista[contador] % 2 == 0:
        pares.append(lista[contador])
    else:
        impares.append(lista[contador])
    
print(f'{lista}')
print(f'{pares}')
print(f'{impares}')
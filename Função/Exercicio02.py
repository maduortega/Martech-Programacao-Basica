from math import sqrt

# Programa que calcula as raízes de um equação do 2° grau 

def calcular_delta():
    delta = b * b - 4 * a * c
    return delta

def calcular_raiz():
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2

# Principal

a = float(input('Informe o valor de a: '))
if a == 0:
    print('NUM PODE SER 0 NÃOOOOO')
else:
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    delta = calcular_delta()
    if delta < 0:
        print('A equação não tem raiz real (MADRID)')
    else:
        x1, x2 = calcular_raiz()
        print(f'x1 = {x1: .2f}')
        print(f'x2 = {x2: .2f}')
# Usando a biblioteca (operações) criada por nós

import Operacoes

a = float(input('Informe o valor de a: '))
if a == 0:
    print('Não é uma equação do 2° grau.')
else:
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    delta = Operacoes.calcular_delta(a, b, c)
    if delta < 0:
        print('Não tem raíz real (MADRIIIID)')
    else:
        x1, x2 = Operacoes.calcular_raiz(a, b, delta)
        print(f'x1 = {x1: .2f}')
        print(f'x2 = {x2: .2f}')
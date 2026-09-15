from math import sqrt

# Dentro da biblioteca não tem entrada e saída de dados!

# Função para calcular o valor do delta

def calcular_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

# Função para calcular e retornar o valor das raízes de uma equeção do 2° grau

def calcular_raiz(a, b, delta):
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2

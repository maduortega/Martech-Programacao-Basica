def ler_dados():
    dados = []
    qtd = int(input('Informe a quantidade de pessoas: '))
    for _ in range (qtd):
        nome = input('Informe o nome da pessoa: ')
        idade = int(input('Informe a idade dele(a): '))
        dados.append((nome, idade))
    return dados

def imprimir_maior_25(dados):
    for nome, idade in dados:
        if idade > 25:
            print((nome), (idade))
            
def media(dados):
    soma = sum(idade for _, idade in dados)
    media = soma / len(dados)
    print(f'{media: .0f}')
            
dados = ler_dados()
imprimir_maior_25(dados)
print('---------------------')
media(dados)
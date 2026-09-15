def febre():
    for i in range(len(temp)):
        if (temp[i]) > 37.8:
            print(f'O(a) paciente {nome[i]} está com febre, com {temp[i]}C°')

def risco():
    for i in range(len(nome)):
        if (temp[i]) <= 37.5 and (pressao[i]) <= 130:
            print(f'O risco do(a) paciente {nome[i]} é BAIXO. Temperatura: {temp[i]}, Pressão: {pressao[i]}')
        elif (temp[i]) > 38.5 or (pressao[i]) > 150:
            print(f'O risco do(a) paciente {nome[i]} é ALTO. Temperatura: {temp[i]}, Pressão: {pressao[i]}')
        else:
            print(f'O risco do(a) paciente {nome[i]}, é MODERADO. Temperatura {temp[i]}, Pressão: {pressao[i]}')

qtd_p = int(input('Informe a quantidade de pacientes: '))

temp = []
pressao = []
nome = []

for i in range(qtd_p):
    nome.append(input('Informe o nome do paciente: '))
    pressao.append(float(input('Informe a pressão do paciente: ')))
    temp.append(float(input('Informe a temperatura do paciente: ')))
    print()
    
    febre()
    risco()
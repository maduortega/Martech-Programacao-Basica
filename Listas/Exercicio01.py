def media_dia():
    for i in range(len(sensor1)):
        media = (sensor1[i] + sensor2[i]) / 2
        print(f'Média do dia {i + 1} = {media}C°')
        if media > 25:
            print('Alerta vermelho.')

def media_sem():            # Média da semana = média das médias
    media_semana = 0
    for i in range(len(sensor1)):
        media = (sensor1[i] + sensor2[i]) / 2
        media_semana += media
    media_semana /= len(sensor1)
    print(f'A média semanal é de = {media_semana: .2f}C°')
    
sensor1 = [] # Variáveis globais (visível em todo o código)
sensor2 = []

for i in range (7):
    sensor1.append(float(input('Informe a temperatura do dia capturada no sensor 1: ')))
    sensor2.append(float(input('Informe a temperatura do dia capturada no sensor 2: ')))
    print()
    
    media_dia()
    print()
media_sem()
def media_dia():
    for i in range(len(sensor1)):
        media = (sensor1[i] + sensor2[i]) / 2
        print(f'A média do dia é: {i + 1} = {media}')

def media_sem():
    media_semana = 0
    for i in range(len(sensor1)):
        media = (sensor1[i] + sensor2[i]) / 2
        media_semana += media
    print(f'Total acumulado durante a semana = {media_semana}mm')

def alerta():
    media_semana = 0
    for i in range(len(sensor1)):
        media = (sensor1[i] + sensor2[i]) / 2
        media_semana += media
    if media_semana <= 100:
        print(f'Não há alertas! Preciptação acumulada (em mm): {media_semana}')
    elif media_semana > 300: 
        print(f'Alerta vermelho! Preciptação acumulada (em mm): {media_semana}')
    elif media_semana < 201 and media_semana > 100:
        print(f'Alerta Amarelo! Preciptação acumulada (em mm): {media_semana}')
    else:
        print(f'Alerta Laranja! Preciptação acumulada (em mm): {media_semana}')

sensor1 = []
sensor2 = []

for i in range(7):
    sensor1.append(float(input('Qual o volume da chuva capturada pelo sensor 1? (em mm): ')))
    sensor2.append(float(input('Qual o volume da chuva capturada pelo sensor 2? (em mm): ')))
    print()
    
    media_dia()
    print()
    
media_sem()
alerta()
x = {'Mario': 64, 'Mk': 11, 'Red dead': 2}


# Imprime apenas os nomes dos jogos

for jogo in x:
    print(f'{jogo}')
    
# Imprime apenas o complemento dos jogos

for jogo in x.values():
    print(f'{jogo}')
    
# Imprime o complemento e os jogos

for jogo, complemento in x.items():
    print(f'{jogo} {complemento}')
    
# Imprimir os jogos com os complementos que sejam maiores que 10

for jogo, complemento in x.items():
    if complemento > 10:
        print(f'{jogo} {complemento}')
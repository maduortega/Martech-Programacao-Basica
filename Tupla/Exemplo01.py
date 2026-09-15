lista = [('Johnny', 21),('Brad', 20),('Dicaprio', 17),('Dacre', 23)]

for i in range(len(lista)):
    nome, idade = lista[i] #só funciona no py / i para percorrer e ir rodando a lista cada vez
    if idade > 18:
        print(f'{nome} {idade}') 
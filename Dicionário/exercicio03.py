# imprima o nome do aluno com a maior nota

alunos = {'Ana': 6, 'Bruno': 8, 'Carlos': 9}
maior_nota = 0

for nome, nota in alunos.items():
    if nota > maior_nota:
        maior_nota = nota
        nome_aluno = nome
print(f'O aluno com a maior nota é: {nome_aluno} {maior_nota}')


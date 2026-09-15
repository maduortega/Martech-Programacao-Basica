# Imprimindo o nome do paciente e seu IMC

lista = [('PacientePython', 1.88, 78), ('PacienteJava', 1.70, 90), ('PacienteC++', 1.90, 65)]

for i in range(len(lista)):
    nome, altura, peso = lista[i]
    imc = peso / (altura * altura)
    print(f'O paciente {nome} Tem o IMC de{imc: .2f}')
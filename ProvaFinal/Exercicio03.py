def variacao():
    for i in range(len(nome)):
        porcentagem = (v_fechamento[i] - v_abertura[i]) / v_abertura[i] * 100
        print(f'A ação {nome[i]} tem a seguinte porcentagem: {porcentagem: .2f}%') # Obs: .2f arredonda a porcentagem
            
    
def sim_retorno():
    for i in range(len(nome)):
        porcentagem = ((v_fechamento[i] - v_abertura[i]) / v_abertura[i]) * 100
        
        if porcentagem < 0:
            porcent2 = -100 * porcentagem / 100 # Tirando o -6.66, deixando positivo
            investimento = 1000 - porcent2
            
        elif porcentagem > 0:
            porcent3 = 100 * porcentagem / 100
            investimento = 1000 + porcentagem  # não consegui fazer a soma para somar a porcentagem mesmo
        
        print(f'A simulação de retorno de um investimento hipotético de R$ 1000,00 nessa ação é: {investimento: .2f}')
 
# Faltou a função de maior e menor lucro (ação) 
    
nome = []
v_abertura = []
v_fechamento = []

qtd = int(input('Quantas ações serão analisadas? '))

for i in range(qtd):
    nome.append(input('Informe o nome de ação: '))
    v_abertura.append(float(input('Infome o valor da ação na abertura do mercado (início do dia): ')))
    v_fechamento.append(float(input('Informe o valor da ação no fechamento do mercado (final do dia): ')))
    print()
     
    variacao()
    print()
    sim_retorno()
    print()
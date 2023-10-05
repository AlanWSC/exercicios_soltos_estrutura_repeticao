#Altere o programa anterior para mostrar no final a soma dos números.

#Faça um programa que receba dois números inteiros e 
#gere os números inteiros que estão no intervalo compreendido por eles.

soma = 0
while True:
    num_menor = int(input('Digite um número: '))
    num_maior = int(input('Digite um número maior que o anterior: '))

    if num_menor < num_maior:
        for x in range(num_menor, num_maior+1):
            soma += x
            print(x)
        print(f'Resultado da soma: {soma}')
        break
    else:
        print('Erro no cálculo!\nDigite Novamente...\n')
        continue
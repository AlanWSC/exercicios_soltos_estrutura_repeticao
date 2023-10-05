#Faça um programa que receba dois números inteiros e 
#gere os números inteiros que estão no intervalo compreendido por eles.

while True:
    num_menor = int(input('Digite um número: '))
    num_maior = int(input('Digite um número maior que o anterior: '))

    if num_menor < num_maior:
        for x in range(num_menor, num_maior+1):
            print(x)
        break
    else:
        print('Erro no cálculo!\nDigite Novamente...\n')
        continue
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

lista = []
num = int(input('Digite um número inteiro: '))

if num <= 1:
    print(f'{num} não é um número primo.')
else:
    divisor = 0
    for i in range(2, num):
        if num % i == 0:
            divisor += 1
            lista.append(i)

    if divisor == 0:
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.\nLista de números: {lista}')

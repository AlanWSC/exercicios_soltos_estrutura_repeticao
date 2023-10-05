#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

from math import inf 
quant_num = int(input('Quantos números deseja colocar?\n'))

maior = -inf
menor = inf
soma = 0

for x in range(quant_num):
    num = int(input('Digite um número: '))

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    soma += num
   
print(f'Maior número: {maior}\nMenor Número: {menor}\nSoma dos números: {soma}')
    


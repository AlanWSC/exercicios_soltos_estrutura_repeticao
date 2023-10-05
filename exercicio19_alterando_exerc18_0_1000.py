#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

from math import inf

quant_num = int(input('Quantos números deseja colocar?\n'))

maior = -inf
menor = inf
soma = 0

for x in range(quant_num):
    num = int(input('Digite um número: '))

    if num < 0 or num > 1000:
        print(f'O número {num} não foi aceito, pois precisa estar entre 0 e 1000')

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

        soma += num
   
print(f'Maior número: {maior}\nMenor Número: {menor}\nSoma dos números: {soma}')
    


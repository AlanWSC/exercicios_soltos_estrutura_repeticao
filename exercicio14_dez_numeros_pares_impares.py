#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.

quant_par = 0
quant_impar = 0

for x in range(1,11):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        quant_par += 1
    else:
        quant_impar += 1

print(f'Quantidade de números pares: {quant_par}\nQuantidade de número ímpares {quant_impar}')


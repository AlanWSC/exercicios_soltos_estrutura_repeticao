#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Digite um número para calcular o fatorial: '))
fat = 1

for number in range(fat,num+1):
    fat *= number
    number + 1
print(fat)
#Faça um programa que calcule e mostre a média aritmética de N notas.

n_notas = int(input('Digita a quantidade de notas a ser inseridas: '))
soma = 0

for i in range(1, n_notas + 1):
    nota = float(input('Digite a nota: '))
    soma += nota

print(f'A média é: {soma/n_notas}')

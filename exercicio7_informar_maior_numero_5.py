#Faça um programa que leia 5 números e informe o maior número.

maior_numero = 0

for x in range(5):
    x +=1
    valor = int(input('Digite um valor: '))
    if valor > maior_numero:
        maior_numero = valor
        
print(f'Este é o maior número: {maior_numero}')
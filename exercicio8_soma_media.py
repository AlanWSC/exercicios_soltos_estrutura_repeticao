#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for x in range(5):
    x +=1
    valor = int(input('Digite um valor: '))
    soma += valor
    media = soma / 5
        
print(f'Esta é a soma dos números: {soma}\nEsta é a média dos números: {media}')
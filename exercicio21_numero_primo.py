#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número inteiro: '))

if num <= 1:
    print(f'{num} não é um número primo.')
else:
    divisor = 0
    for i in range(2, num):
        if num % i == 0:
            divisor += 1
            break  
        
    if divisor == 0:
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')

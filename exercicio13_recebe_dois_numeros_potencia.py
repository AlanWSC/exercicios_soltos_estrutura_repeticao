#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem.

base = int(input('Digite um número para base: '))
expoente = int(input('Digite um número para o expoente: '))

print(f'{base} ^ {expoente} = {base ** expoente}')
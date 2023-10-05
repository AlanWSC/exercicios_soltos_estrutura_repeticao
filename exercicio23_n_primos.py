#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input('Digite um número: '))
n_divisoes = 0  

if num <= 1:
    print(f'O número {num} não é primo')
else:
    for i in range(2, num + 1):
        if i > 1:
            is_prime = True
            for j in range(2, i):
                n_divisoes += 1
                if (i % j == 0):
                    is_prime = False
                    break
            if is_prime:
                print(i)

print(f'Número de divisões realizadas: {n_divisoes}')

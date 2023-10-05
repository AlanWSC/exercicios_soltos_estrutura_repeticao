#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular 
#o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


while 1 == 1:
    num = int(input('Digite um número para calcular o fatorial:  '))

    if num < 1 or num > 16:
        print('Tente novamente!\nInsira números entre 1 e 16')
    
    else:
        fat = 1 #A variavel precisa ser reiniciada todas as vezes
        for number in range(fat,num+1):
            fat *= number
            number + 1
            print(fat)
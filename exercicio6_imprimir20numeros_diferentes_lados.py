#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

pergunta = input('Deseja imprimir em (h)(H) - Horizontal ou (v)(V) - Vertical?\n')

if pergunta == 'h' or pergunta == 'H':
    
    for x in range(20):
        x += 1
        print(f'{x}', end=' ')
elif pergunta == 'v' or pergunta == 'V':
    for x in range(20):
        x += 1
        print(f'{x}')
else:
    print('Digite uma opção válida')




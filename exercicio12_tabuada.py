#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada. 

numero = int(input('Digite um numero inteiro para calcular a tabuada: '))

for x in range(1,11): print(f'{x} * {numero} = {x * numero}')
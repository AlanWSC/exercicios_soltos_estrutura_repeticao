#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera 
#verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n_pessoas = int(input('Digite a quantidade de idades que serão inseridas: '))
soma_idade = 0

for idade in range(1, n_pessoas + 1):
    idade = int(input('Digite a idade: '))
    soma_idade += idade

resultado = soma_idade/n_pessoas

if resultado > 0 or resultado <= 25:
    print(f'A média de idade é: {resultado}\nPortanto, a turma é jovem.')

elif resultado > 25 or resultado <= 60:
    print(f'A média de idade é: {resultado}\nPortanto, a turma é adulta.')

elif resultado > 60:
    print(f'A média de idade é: {resultado}\nPortanto, a turma é idosa.')

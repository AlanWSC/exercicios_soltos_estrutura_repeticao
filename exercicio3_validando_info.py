#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    name = input('Digite seu nome: ')
    if len(name) < 4:
        print('Digite seu nome com no mínimo 4 caracteres')
    else:
        break

while True:
    age = int(input('Digite sua idade: '))
    if age < 0 or age > 150:
        print('Idade inválida, digite novamente.')
    else:
        break

while True:
    money = float(input('Digite o seu salário mensal: '))
    if money < 1200:
        print('Seu salário está baixo!')
    else:
        break

while True:
    sex = input('Digite:\n(f) - Feminino\n(m) - Masculino\n')
    if sex != 'f' and sex != 'm':
        print('Sexo inválido, digite novamente')
    else:
        break

while True:
    estado_civil = input('Digite:\n(s) - Solteiro\n(c) - Casado\n(v) - Viuvo\n(d) - Divorciado\n')
    if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        print('Estado civil inválido, digite novamente.')
    else:
        break

print('Informações válidas:')
print('Nome:', name)
print('Idade:', age)
print('Salário:', money)
print('Sexo:', sex)
print('Estado Civil:', estado_civil)

#Faça um programa que leia um nome de usuário e a sua senha 
#e não aceite a senha igual ao nome do usuário, mostrando uma 
#mensagem de erro e voltando a pedir as informações.

while True:
    login = input('Digite seu login:\n')
    password = input('Digite sua senha:\n')

    if login != password:
        break
    print(f'Erro! Login e Password não podem ser iguais')
    
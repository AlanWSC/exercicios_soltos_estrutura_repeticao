#Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

while True:

    while True:
        populacaoA = input('Digite a população A: ')
        if not populacaoA.isdigit():
            print('Digite apenas números inteiros')
        else:
            populacaoA = int(populacaoA)
            break

    while True:
        populacaoB = input('Digite a população B: ')
        if not populacaoB.isdigit():
            print('Digite apenas números inteiros')
        else:
            populacaoB = int(populacaoB)
            break

    while True:
        taxaCrescimentoA = input('Digite a taxa de crescimento da população A: ')
        if not taxaCrescimentoA.replace(".", "").isdigit():
            print('Digite apenas números')
        else:
            taxaCrescimentoA = float(taxaCrescimentoA) /100
            break

    while True:
        taxaCrescimentoB = input('Digite a taxa de crescimento da população A: ')
        if not taxaCrescimentoB.replace(".", "").isdigit():
            print('Digite apenas números')
        else:
            taxaCrescimentoB = float(taxaCrescimentoB) / 100
            break

    anos = 0

    while populacaoA <= populacaoB:
        populacaoA *= (1 + taxaCrescimentoA)
        populacaoB *= (1 + taxaCrescimentoB)
        anos += 1
        #print(f'Ano: {anos}\nPopulação A: {populacaoA:.2f}\nPopulação B: {populacaoB:.2f}\n')

    print(f"Levou {anos} anos para a população do país A ultrapassar ou igualar a população do país B.")

    continuacao = input('Deseja fazer outra operação?\n')
    if continuacao != 's' and continuacao != 'S':
        break
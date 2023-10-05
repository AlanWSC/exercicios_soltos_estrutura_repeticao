#Supondo que a população de um país A seja da ordem de 80000 habitantes 
#com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
#com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número 
#de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
#mantidas as taxas de crescimento.

populacaoA = 80000
populacaoB = 200000

taxaCrescimentoA = 0.03  # 3% de crescimento
taxaCrescimentoB = 0.015  # 1.5% de crescimento

anos = 0

while populacaoA <= populacaoB:
    populacaoA *= (1 + taxaCrescimentoA)
    populacaoB *= (1 + taxaCrescimentoB)
    anos += 1
    #print(f'Ano: {anos}\nPopulação A: {populacaoA:.2f}\nPopulação B: {populacaoB:.2f}\n')

print(f"Levou {anos} anos para a população do país A ultrapassar ou igualar a população do país B.")

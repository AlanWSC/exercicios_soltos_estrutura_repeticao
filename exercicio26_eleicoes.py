#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print('Eleições 2022\n')

num_eleitores = int(input('Digite a quantidade de eleitores que irão votar: '))

faz_o_L = 0
faz_a_arminha = 0
te_tiro_do_serasa = 0

for i in range(1, num_eleitores + 1):
    print('1 - Candidato faz o L\n2 - Candidato faz a arminha\n3 - Candidato te tiro do serasa')

    voto = int(input('Vote no número do seu candidato: '))
    print('\n')

    if voto == 1:
        faz_o_L += 1

    elif voto == 2:
        faz_a_arminha += 1
    
    elif voto == 3:
        te_tiro_do_serasa += 1
    
    else:
        print('Número incorreto')

print(f'Resultado final\
      \n1 - Candidato faz o L\nObteve {faz_o_L} voto(s)\n\n\
      \n2 - Candidato faz a arminha\nObteve {faz_a_arminha} Voto(s)\n\n\
      \n3 - Candidato te tiro do serasa\nObteve {te_tiro_do_serasa} Voto(s)')
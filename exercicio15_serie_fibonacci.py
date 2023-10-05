#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.

primeiro, segundo = 1, 1

termo = int(input('Digite um número: '))

if termo == 1 or termo == 2:
    print(1)

else:

    for fib in range(3, termo+1):
        termo = primeiro + segundo
        segundo = primeiro
        primeiro = termo
        fib += 1
        print(termo)
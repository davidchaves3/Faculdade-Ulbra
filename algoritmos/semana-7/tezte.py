import random

c = 0
num = 0
resp = 's'
sorte = random.randint(1, 100)
print('Adivinhe o número ')
print(sorte)

while resp == 's':

    num = int(input('digite um número ==>'))
    c = c + 1
    if sorte < num:
        print('O número é menor')

    elif sorte > num:
        print('O número é maior')

    else:
        print('acertou!')
        print('O número era {}'.format(sorte))
        print('Qtd de tentativas ==>{}'.format(c))
        resp = input('Jogar novamente?[S/N]')

print('JOGO FINALIZADO')
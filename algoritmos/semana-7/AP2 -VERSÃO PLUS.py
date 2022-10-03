# EQUPE 6 🔥😎 - David, Arthur, Maeyve, Savio Ramon

import random
cont = 0
numeroDigitado = 0
resposta = 's'
numeroSorteado = random.randint(1, 100)
print('==============JOGO DE ADIVINHAÇÃO==============\n')
print('               Adivinhe o número               \n')
print('===============================================\n')

while resposta == 's' or resposta == 'S':

    numeroDigitado = int(input('digite um número ===>'))
    cont = cont + 1

    if numeroSorteado < numeroDigitado:
        print('===============================================\n')
        print('O número sorteado é menor que o digitado!')
        print('===============================================\n')

    elif numeroSorteado > numeroDigitado:
        print('===============================================\n')
        print('   O número sorteado é maior que o digitado!   \n')
        print('===============================================\n')

    else:
        print('===============================================\n')
        print('Parabéns!!!! Você acertou o número sorteado!')
        print('O número sorteado era {}'.format(numeroDigitado))
        print('Quatidade de tentativas {}'.format(cont))
        print('===============================================  ')
        resposta = input('Jogar novamente?[S/N]')
        print('===============================================  ')

        if resposta == 's' or resposta == 'S':
            numeroSorteado = random.randint(1, 100)
            cont = 0

print('**********************************************************\n')
print('                     JOGO FINALIZADO                       \n')
print('**********************************************************  ')

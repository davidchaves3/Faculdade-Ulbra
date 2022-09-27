import random

cont = 0
numeroDigitado = 0
resposta = 's'
numeroSorteado = random.randint(1, 100)

print('Adivinhe o número ')
while resposta == 's' or resposta == 'S':

    numeroDigitado = int(input('digite um número :'))
    cont = cont + 1
    
    if numeroSorteado < numeroDigitado:
        print('O número sorteado é menor que o digitado!')

    elif numeroSorteado > numeroDigitado:
        print('O número sorteado é maior que o digitado!')

    else:
        print('******************************************')
        print('Parabéns!!!! Você acertou o número sorteado!')
        print('O número sorteado era {}'.format(numeroDigitado))
        print('Quatidade de tentativas {}'.format(cont))
        print('******************************************')
        resposta = input('Jogar novamente?[S/N]')
        
        if resposta == 's' or resposta == 'S':
            numeroSorteado = random.randint(1,100)
            cont = 0
            
print('JOGO FINALIZADO')

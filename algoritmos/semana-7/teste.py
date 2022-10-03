import random

resposta = 'S'
numeroDigitado = 0
numeroSorteado = random.randint(1, 100)
print(numeroSorteado)

while resposta == 's' or resposta == 'S':
    numeroDigitado = int(input('Digite um número:'))

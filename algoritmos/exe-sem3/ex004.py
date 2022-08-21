num = float(input('Digite um número:'))

if num > 0 :
    print('É um número positivo')
    print('Dobro do número é igual a', num * 2)
elif num < 0 :
    print('Número negativo')
    if num %2 == 0 :
            print('número par')
    else :
            print('número negativo')
else :
    print('número é zero')

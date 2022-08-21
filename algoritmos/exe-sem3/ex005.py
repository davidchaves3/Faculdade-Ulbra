valor1 = int(input('digite um número:'))
valor2 = int(input('Digite outro:'))
cond = input('qual tipo de código [D/C]')

if cond == 'c' or cond == 'C' :
    if valor1 > valor2 :
        print(valor2)
        print(valor1)
    elif valor1 < valor2 :
        print(valor1)
        print(valor2)
    else :
        print('números são iguais!')
elif cond == 'd' or cond == 'D' :
    if valor1 > valor2:
        print(valor1)
        print(valor2)
    elif valor1 < valor2 :
        print(valor2)
        print(valor1)
    else :
        print('Números são iguais')
elif cond != 'C' or cond != 'c' :
    print('Opção inválida')
elif cond != 'D' or cond != 'd' :
    print('Opção inválida')

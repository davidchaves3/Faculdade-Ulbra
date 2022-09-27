import random
# VARIÁVEIS 
cont = 0
numeroDigitado = 0
resposta = 's'
numeroSorteado = random.randint(1, 100)

print('Adivinhe o número ')
#Laço de Repetição
while resposta == 's' or resposta == 'S':
#Entrada de Dados 
    numeroDigitado = int(input('digite um número :'))
    cont = cont + 1
                                                                 #Verifica se o número digitado É maior que número sorteado|
    if numeroSorteado < numeroDigitado:                          #se for false ele passa para a proxima codição
                                                                 #caso a condição seja true, ira parece a mensagem
        print('O número sorteado é menor que o digitado!')
                                          

    elif numeroSorteado > numeroDigitado:                        #Aqui vai verificar se o número sorteado e maior que o digitado                
        print('O número sorteado é maior que o digitado!')       #se for false ele passa para a proxima codição
                                                                 #caso a condição seja true, ira parece a mensagem  

    else:
        
        print('******************************************')      #Caso as demais condições seja false, que quer que o usuario acertou o número
        print('Parabéns!!!! Você acertou o número sorteado!')    #Então vai em imprimir os print colocados
        print('O número sorteado era {}'.format(numeroDigitado))
        print('Quatidade de tentativas {}'.format(cont))
        print('******************************************')
        
        resposta = input('Jogar novamente?[S/N]')                #Condicional, ele digitando 'N' o laço vai encerrar.
        
        if resposta == 's' or resposta == 'S':                   #caso ele Digite 'S' vai gerar um novo número aleatório 
            numeroSorteado = random.randint(1,100)               # É o cont será zerado
            cont = 0                                             # Loop irá  acontecer até o usuário Digita 'N'
            
print('JOGO FINALIZADO')

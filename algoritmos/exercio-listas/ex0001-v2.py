#Declaração De variáveis
cont = 0 
listaNum = []
num = 0 
qtdItem = 0
#Laço de Repetição 
while cont < 6 :
  num = listaNum.append(int(input("Digite um número inteiro ==>"))) #Entrada de Dados / Números inteiros
  cont = cont + 1
  qtdItem = len(listaNum)
#Saída de Dados
  if cont == 6 :
    qtdItem = len(listaNum)
    print("\n=============== TODOS OS NÚMEROS ===============")
    print("{}\n{}\n{}\n{}\n{}\n{}".format(listaNum[0],listaNum[1],listaNum[2],listaNum[3],listaNum[4],listaNum[5]))
    print("\n=================================================") 
    print("\n============= 3 PRIMEIROS NÚMEROS ===============")
    print("{}\n{}\n{}".format(listaNum[0],listaNum[1],listaNum[2]))

print("\n=================FINALIZADO===================")
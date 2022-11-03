cont = 0 
listaNum = []

while cont < 6 :
  num =listaNum.append(int(input("Digite um número inteiro:")))
  cont = cont + 1 

print("\n=================== TODOS OS NÚMEROS ===================")
cont = 0

while cont < len(listaNum) :
  print(listaNum[cont])
  cont = cont + 1 

cont = 0 

print("\n=================== 3 PRIMEIROS NÚMEROS ===================\n")

while cont < 3 :
  print(listaNum[cont])
  print("====================================================\n")
  cont = cont + 1




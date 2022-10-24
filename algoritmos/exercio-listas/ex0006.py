listNumber = []
listPositionP = []
listPositionN = []
cont = 0

num = int(input("Digite um número ou Digite Zero para encerrar:"))

while num != 0 :
  listNumber.append(num)
  num = int(input("Digite um número ou Digite Zero para encerrar:")) 

print("Lista Criada:\n{}".format(listNumber))

while cont < len(listNumber):
  if listNumber[cont] > 0 :
    listPositionP.append(cont)
  elif listNumber[cont] < 0 :
    listPositionN.append(cont)

print("Lista com sinais Trocados:\n{}".format(listNumber))
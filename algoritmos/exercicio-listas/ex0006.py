listNumber = []
cont = 0
print("===================================================")
num = int(input("Digite um número ou Digite Zero para encerrar:"))
print("===================================================")

while num != 0 :
  listNumber.append(num)
  print("===================================================")
  num = int(input("Digite um número ou Digite Zero para encerrar:"))
  print("===================================================")
print("Lista Criada:\n{}".format(listNumber))
print("===================================================")

while cont < len(listNumber):
  listNumber[cont] = listNumber[cont] * -1
  cont = cont + 1
print("===================================================")
print("Lista com sinais Trocados:\n{}".format(listNumber))
print("===================================================")
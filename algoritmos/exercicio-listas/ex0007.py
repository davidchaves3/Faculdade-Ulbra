listNumber = []
resp = "S"
cont = 0

while resp == "S" or "s":
  listNumber.append(float(input("Digite um número real:")))
  resp = input("Continuar?")


print("Lista Criada:\n{}".format(listNumber))

while cont < len(listNumber):
  if cont < 5:
    listNumber.insert(cont,2 * listNumber[cont])
  elif cont > 4:
    listNumber.insert(cont,2 / listNumber[cont])
  cont = cont + 1

print(listNumber)
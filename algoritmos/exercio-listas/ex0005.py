listNumber = [-5,10,-8,-3,5,10,11,8,-9,10]
numberPositivo = []
numberNegativo = [] 
cont = 0

while cont < len(listNumber):
  if listNumber[cont] > 0:
    numberPositivo.append(listNumber[cont])
  elif listNumber[cont] < 0:
    numberNegativo.append(listNumber[cont])
  cont = cont + 1

print("================================================")
print("Numeros Positivos:\n {}".format(numberPositivo))
print("================================================")
print("Numeros Negativos:\n {}".format(numberNegativo))
print("================================================")


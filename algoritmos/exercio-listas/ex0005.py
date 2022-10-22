listNumber = [-5,10,-8,-3,5,10,11,8,-9,10]
numberPositivo = []
numberNegativo = [] 
cont = 0
while cont < len(listNumber):
  if len(listNumber[cont]) > 0 :
    numberPositivo.append(listNumber[cont])
  elif len(listNumber[cont]) < 0 :
    numberNegativo.append(listNumber[cont])

print("Numeros Positivos:")
print(numberPositivo)
print("Numeros Negativos:")
print(numberNegativo)

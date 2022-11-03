lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
numberPares = []
cont = 0
maior = 0
somaP = 0

while cont < len(lista):
  number = lista[cont]
  if number > 0 :
    somaP = somaP + number
  if number > maior:
    maior = number
  if number%2 == 0 :
    numberPares.append(cont)
  cont = cont + 1

print("========================================")
print("========================================")
print("Os 5 primeiros elementos: \n{}\n{}\n{}\n{}\n{}".format(lista[0],lista[1],lista[2],lista[3],lista[4]))
print("========================================")
print("A soma dos elementos Positivos:\n{}".format(somaP))
print("========================================")
print("A posição dos elemento pares:\n{}".format(numberPares))
print("========================================")
print("O maior elemento da lista:\n{}".format(maior))
print("============= FINALIZADO ===============")

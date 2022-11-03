listNumber = [0,20,4,36,40,22,25,30,80,88,90,21,40,98,66]
impares = []
pares = []
cont = 0

while cont < len(listNumber):
  if cont%2 == 0 :
    impares.append(listNumber[cont])
  else :
    pares.append(listNumber[cont])
  cont = cont + 1

print("==========================================================")
print(f"Lista completa {listNumber}")
print(f"Lista dos números que estão em posição pares{pares}")
print(f"Lista dos números que estão em posições ímpares{impares}")
print("==========================================================")


number = [0,1,2,3,4,5,6,7]
cont = 0
if len(number)%2 == 0 :

  while cont < len(number):
    aux = number[cont]
    number[cont] = number[cont + 1]
    number[cont + 1] = aux
    cont = cont + 2

  print(f"Lista com as posições trocadas {number}")

else:
  print("Lista não tem tamanho correto!")
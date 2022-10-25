number = [5,7,3,2,8,10,9,9]
auxiliar = 0
auxiliar2 = 0
cont = 0

if len(number) %2 == 0:
  while cont < len(number):
    if number[cont] %2 == 0:
     auxiliar = number[cont]
     auxiliar2 = number[cont + 1]
    
     number[cont] = auxiliar2
     number[cont + 1] = auxiliar
      
  print(number)
else:
  print("Lista não tem tamanho correto!!")
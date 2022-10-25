number = [5,7,3,2,8,10,9]
cont = 0
auxiliar = 0

if len(number) %2 == 0:
  while cont < len(number):
    if cont %2 == 0:
      auxiliar = number[cont]
    else:
      number = auxiliar
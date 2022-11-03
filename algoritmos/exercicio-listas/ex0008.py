listNumber = []
maior = 0  
menor = 0 
cont =  0 
somaDos10 = 0 
qtPares = 0

print("================================================================")
num = int(input(("Digite um número ou Digite zero para encerrar!")))
while num != 0:
  if num %2 == 0 :
    qtPares = qtPares + 1

  if num < menor :
    menor = num

  if cont < 10 :
    somaDos10 = somaDos10 + num

  cont = cont + 1
  listNumber.append(num)
  print("================================================================")
  num = int(input(("Digite um número ou Digite zero para encerrar!")))
  print("================================================================")
  
print("================================================================")
print(f"Quantidade de números pares{qtPares}\n")
print(f"O maior elemento da Lista {menor}\n")
print(f"A soma dos 10 primeiros elementos {somaDos10}\n")
print(f"Lista completa{listNumber}zn")
print("================================================================")
listNumber = []
qtPares = 0
maior,menor , cont , somaDos10 = 0


num = int(input(("Digite um número ou Digite zero para encerrar!")))
while num != 0:
  if num %2 == 0 :
    qtPares = qtPares + 1
  if num > maior :
    maior = num
  if num < menor :
    menor = num
  if cont < 10 :
    somaDos10 = somaDos10 + num
  cont = cont + 1
  listNumber.append(num)
  num = int(input(("Digite um número ou Digite zero para encerrar!")))
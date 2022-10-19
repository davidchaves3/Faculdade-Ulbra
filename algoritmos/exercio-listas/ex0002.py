from turtle import position


listNum = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
maior = 0 
cont = 0 
somaPositivo = 0
position = []
tamanhoLista = 0

while cont < len(listNum):
  num = listNum[cont]
  tamanho = len(listNum)
  
  if num > maior :
    maior = num 
  if num > 0 :
    somaPositivo = somaPositivo + num
    position.append(listNum[cont])
  cont = cont + 1
  if cont == tamanho :
    print("Finalizado")
  

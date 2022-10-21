lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
listaPositivo = []
cont = 0
maior = 0

while cont < len(lista):
  number = len(lista[cont])
  if number > 0 :
    somaP = somaP + number
  if number > maior:
    maior = number
  if number%2 == 0 :
    listaPositivo.append(cont)
  
print( 
  "Os 5 primeiros elementos: \n{}\n{}\n{}\n{}\n{}\n",
  "A soma dos elementos:\n{}\n",
  "A posição dos elemento pares:\n{}\n",
  "O maior elemento da lista:\n{}"
  .format(lista[0],lista[1],lista[2],lista[3],lista[4],somaP,listaPositivo,maior)
  )

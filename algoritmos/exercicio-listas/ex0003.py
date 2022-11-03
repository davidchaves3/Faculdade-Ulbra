lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
cont = 0
listaNumber = []

print("============================================")
user = int(input("Digite um número:"))
print("============================================")

while cont < len(lista):
  if user in lista:
    if user == lista[cont]:
     listaNumber.append(lista[cont])
  cont = cont + 1
if user in lista:
  print("============================================")
  print("Esse número existe na lista")
  print("Ele aparecer {} na lista".format(len(listaNumber)))
  print("============================================")
else:
  print("============================================")
  print("Número não existe na lista")
  
print("================= FINALIZADO ===============")
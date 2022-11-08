maior = 0
part = []
parts = []
notaFinal = []
cont = 0
j = 0
# Laço de repetição para entrada de dados dos participantes
while cont < 10:
   # laço de repetição para as três notas
  while j < 3:
    part.append(float(input("NOTA:")))
    notaFinal.append(part[0] + part[1] + part[2])
    j = j + 1
  parts.append(part)
  part = []
# Laço de repetição para imprimir cada nota dos participantes
  if maior < notaFinal[cont]: 
    maior = notaFinal[cont]
  cont = cont + 1

cont = 0
# Laço de repetição para imprimir cada nota dos participantes
while cont < 10: 
  print(f"Código:{cont} NOTAS:{parts[cont]}")
  cont = cont + 1

print("Vencedores:")
cont = 0
#Laço de repetição para percorrer toda a lista e verificar se tem empate nas notas finais dos participantes 
while cont < 10: 
  if notaFinal[cont] == maior:
    print(f"Código:{cont}")
    cont = cont + 1

 

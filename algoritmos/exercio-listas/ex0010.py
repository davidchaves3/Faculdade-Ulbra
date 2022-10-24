listG = ['E','A','B','C','C','D','E','A','C','D']
listR = []
certa = []
errada = []
cont = 0

while cont < 10:
  listR.append(input("Resposta:"))
  cont = cont + 1

cont = 0
while cont < 11:
  if listR[cont] == listG[cont]:
    certa.append(cont + 1)
  else:
    errada.append(cont + 1)
  cont = cont + 1

print("O aluno acertou as questões {}".format(certa))
print("E o aluno errou as questões {}".format(errada))

if len(certa) - len(listG) >= 6:
  print("ALUNO APROVADO!!!!")
else:
  print("ALUNO REPROVADO!!!!")
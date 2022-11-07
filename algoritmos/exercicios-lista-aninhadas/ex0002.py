participantes = []
participante = []
notaFinal = []
cont = 0
maior = 0

while cont < 3 :
  participante.append(float(input("Nota do 1ª Jurado:")))
  participante.append(float(input("Nota do 2ª Jurado:")))
  participante.append(float(input("Nota do 3º Jurado:")))
  notaFinal.append( participante[0] + participante[1] + participante[2])
  participantes.append(participante)
  participante = []
  cont = cont + 1

cont = 0
while cont < len(notaFinal):
  if notaFinal[cont] > maior:
    maior = notaFinal[cont]

cont = 0
while cont < len(participantes):
  print(f"Código Participante {cont} NOTAS - {participantes[cont][0],participantes[cont][1],participantes[cont][2]}")
  cont = cont + 1
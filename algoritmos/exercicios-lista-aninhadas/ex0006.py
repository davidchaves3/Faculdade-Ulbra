signo = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
signoNum = [0,1,2,3,4,5,6,7,8,9,10,11]
usuarios = []
cont = 0
i = 0

while cont < 3:
  dadosIndividual = []
  dadosIndividual.append(input("Nome:"))
  dadosIndividual.append(int(input("Ano de Nascimento:")))
  calc = dadosIndividual[1]%2
  while i < len(signoNum):
    if calc == signoNum[i]:
      dadosIndividual.append(signo[signoNum[i]])
    i = i + 1  
  usuarios.append(dadosIndividual)
  cont = cont + 1

cont = 0
while cont < len(usuarios):
  print(f"{usuarios[cont][0]} Nasceu em {usuarios[cont][1]} e o seu signo chinês é {usuarios[cont][2]}")
  cont = cont + 1
  
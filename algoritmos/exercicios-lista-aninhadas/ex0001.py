funcionarios = []
aprovados = []
func = []
i = 0

while i < 5 :
  func.append(input("Nome:"))
  func.append(input("DEPARTAMENTO:"))
  func.append(float(input("Prova escrita:")))
  func.append(float(input("Prova Prática:")))
  funcionarios.append(func)
  i = i + 1
print(funcionarios)

i = 0 
while i < 5:
  print(funcionarios[i])
  if funcionarios[i][2] + funcionarios[i][3] >= 7 :
    aprovados.append(funcionarios[i][0])
  i = i + 1
print("Aprovados", aprovados)

setor = input("Setor:")
i = 0 
while i < 5:
  if funcionarios[i][1] == setor: # if setor in funcionarios[i]
    print(funcionarios[i][0])



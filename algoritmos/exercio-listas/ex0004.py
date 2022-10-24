listWord = []
cont = 0

print("===========================================")
user = input("Digite uma palavra:")
print("===========================================")

while user != "sair":
  listWord.append(user)
  print("===========================================")
  user = input("Digite outra palvra ou escreva SAIR para encerrar:")
  print("===========================================")

print("===========================================")
print(listWord)
print("===========================================")
word = input("escolha uma palavra da lista:")
print("===========================================")

while  word in listWord:
  if word == listWord[cont]:
    listWord[cont] = "ELIMINADA"
  cont = cont + 1

print("===========================================")
print(listWord)
print("\n================ FINALIZADO ===============\n")
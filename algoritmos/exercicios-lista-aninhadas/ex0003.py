listaVasos = [['V01', 100.00, 50.00]['VO2', 80.00, 25.00]['VO3', 110.00, 60.00]['VO4', 230.00, 100.00]['VO5', 25.00, 30.00]]
cont = 0

while cont < len(listaVasos):
  # soma o segundo item da lista e o terceiro e add um quarto item na sub-lista da lista principal
  listaVasos[cont].append(listaVasos[cont][1] + listaVasos[cont][2])
  #Imprimi o código do Produto e o custo dele
  print(f"Código:{listaVasos[cont][0]} Preço de custo:{listaVasos[cont][3]}")
  #Soma total de custo 
  somaPreco = somaPreco + listaVasos[cont][3] 
  cont = cont + 1

#Calculando a média do preço de custo
media =  somaPreco / len(listaVasos)
print(f"Média de Preço de Cust:{media}")

cont = 0
#Laço de repetição para percorrer toda a lista e verificar qual produto tem o preço menor que a média
while cont < len(listaVasos):
  print(f"Código do produto menor que a média:{listaVasos[cont][0]}")
  cont = cont + 1

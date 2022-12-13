lista = []
lista2 = []
continuar = 's'
cont = 0
somaPares = 0
qtd = 0

while continuar == 's' or continuar == 'S':
    print("="*30) 
    num = int(input("Digite um número:"))
    lista.append(num)
    print("="*30) 
    continuar = input("Deseja incluir mais um numero? S ou N ")

while cont < len(lista):
    if lista[cont]%2 == 0:
        somaPares = somaPares + lista[cont]
    if lista[0] == lista[cont]:
        qtd = qtd + 1
    cont = cont + 1
print("="*30) 
print("Soma dos elementos pares da lista 1 =>" , somaPares)
print("="*30) 
print("Quantidade de elementos da lista 1 =>", len(lista))
print("="*30) 

if qtd == len(lista):
    print("="*30) 
    print("Lista preenchida com o mesmo valor")
    print("="*30) 
cont = 0
if len(lista)%2 == 0 :
    while cont < len(lista)/2:
        lista2.append(lista[cont])
        cont = cont + 1

elif len(lista) == 1:
    cont = 0
    lista2.append(lista) 
else:
    while cont < (len(lista)/2) + 1:
        lista2.append(lista[cont])
        cont = cont + 1
print("="*30) 
print("Lista 2 :", lista2)
print("="*30) 

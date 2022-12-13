cont = 0
naoAss = 0
maisDias = 0
listaDias = []
hospedagens = [["Ana Sila","Doki",10,"sim"],
               ["Beto Lima","Lika",11,"não"],
               ["Caca Reis","Lala",10,"não"],
               ["Dado pain","Hipo",20,"sim"],
               ["Eva Sousa","Toto",12,"sim"],
               ["Guga Paes","Dori",10,"não"]]
print(hospedagens)

while cont < len(hospedagens):
    if hospedagens[cont][3] == "sim":
        hospedagens[cont].append(hospedagens[cont][2] * 15)
    elif hospedagens[cont][3] == "não":
        naoAss = naoAss + 1
        hospedagens[cont].append(hospedagens[cont][2] * 30)
        
    if hospedagens[cont][2] > maisDias:
        maisDias = hospedagens[cont][2]

    if hospedagens[cont][2] > 10:
        listaDias.append(hospedagens[cont][1])
    cont =  cont + 1
cont = 0
while cont < len(hospedagens):
    print("="*35)
    print("Nome do Dono: {} \n Valor da Conta R${} ".format(hospedagens[cont][0], hospedagens[cont][4]))
    cont = cont + 1

print("Qunatidade de não associados:",naoAss)
print("="*35)
print("Maior quantidade de dias que um cachorro passou no hotel: ", maisDias)
print("="*35)
print("Lista dos cachorros que passaram mais de 10 dias no hotel")
print(listaDias)

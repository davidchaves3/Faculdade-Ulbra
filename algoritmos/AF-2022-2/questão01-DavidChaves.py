lista = []
cont = 0
continuar = 's'
media = 0
qtdDespesaVesp = 0
qtdMatutino = 0
totMensal = 0


while continuar == 's' or continuar == 'S':
    ficha = []
    print("="*30)
    turno = input("Turno:")
    ficha.append(turno)
    print("="*30)
    turma = input("Turma:")
    ficha.append(turma)
    print("="*30)
    qtdAlunos = float(input("Quantidade de alunos:"))
    ficha.append(qtdAlunos)
    print("="*30)
    mensalidade = float(input("Mensalidade por alunos R$"))
    ficha.append(mensalidade)
    print("="*30)
    despesa = float(input("Despesa da turma R$"))
    ficha.append(despesa)
    print("="*30)
    receita = ficha[2] * ficha[3]
    ficha.append(receita)
    
    if receita > despesa:
        ficha.append("Gera lucro!")
    elif receita == despesa:
        ficha.append("Arrecada o suficiente para as despesas")
    elif receita < despesa:
        ficha.append("Gera prejuízo!")

    if ficha[0] == "vespertino"  or ficha[0] == "tarde" and (ficha[4] < 500):
        qtdDespesaVesp = qtdDespesaVesp + 1
    if ficha[0] == "matutino" or ficha[0] == "manhã":
        qtdMatutino = qtdMatutino + 1
        totMensal = totMensal + ficha[3]
                     
    lista.append(ficha)
                     
    continuar = input("Cadastrar uma nova  turma S ou N ")
                     
media =totMensal / qtdMatutino
while cont < len(lista):
    print("="*30)
    print("Turma:{} \n Turno: {} \n SITUAÇÕA:{}".format(lista[cont][1], lista[cont][0], lista[cont][6]))
    cont = cont + 1
    
print("="*30)
print("Média das mensalidades das turmas do turno da manhã(matutino) R$", media)
print("="*30)
print("Quantidade de turmas do turno vespertino com despesa menor que R$500 é de ", qtdDespesaVesp)
print("="*30)

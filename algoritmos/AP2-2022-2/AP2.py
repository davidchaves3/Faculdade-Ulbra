totalConsumoResidencial = 0
totalConsumoComercial = 0
consumidoresResidencial = 0
consumidoresComercial = 0

# Entrada de Dados do preço do kwh para cada tipo de consumidor
print("\n=====================================================================\n")
precoResidencial = float(input("Digite o preço do Kw/h para consumidor Residencial: R$"))
precoComercial = float(input("\nDigite o preço do Kw/h para consumidor Comercial: R$"))
print("\n=====================================================================\n")
# Entrada de Dados/ código de Identificação
print("=====================================================================")
codigo = int(input("Digite o seu codigo de Identificação:"))
print("\n=====================================================================\n")
while codigo != 0:

    print("\n=====================================================================\n")
    tipo = input("Qual o tipo de Conta[Residencial/Comercial]")
    print("\n=====================================================================\n")

    if tipo == "Residencial":

        # Entrada da quantidade de kwh/mês
        print("\n=====================================================================\n")
        contaResidencial = float(input("Digite a quantidade de kw/h gasto na sua residência  neste mês:"))
        print("\n=====================================================================\n")

        # total de consumo de Kwh/mês da categoria Residencial
        totalConsumoResidencial = totalConsumoResidencial + contaResidencial
        totalPayResidencial = precoResidencial * \
        contaResidencial  # Valor que consumidor irá pagar
        consumidoresResidencial = consumidoresResidencial + 1

        # Saída de Dados
        print("\n=====================================================================\n")
        print("Código: {} \n Valor total  a pagar R${}".format(codigo, totalConsumoResidencial))
        print("\n=====================================================================\n")

    elif tipo == "Comercial":

        # Entrada da quantidade de kwh/mês
        print("\n=====================================================================\n")
        contaComercial = float(input("Digite a quantidade de kw/h gasto no comercial este mês: "))
        print("\n=====================================================================\n")
        # Calculos
        # total de consumo de Kwh/mês da categoria Comercial
        totalConsumoComercial = totalConsumoComercial + contaComercial
        totalPayComercial = precoComercial * \
        contaComercial  # Valor que consumidor irá pagar
        consumidoresComercial = consumidoresComercial + 1

        # Saída de Dados
        print("\n=====================================================================\n")
        print("Código: {} \n Valor total  a pagar R${}".format(codigo, totalConsumoComercial))
        print("\n=====================================================================\n")
    else:
        # Saída de Dados
        print("\n=====================================================================\n")
        print(
            "TIPO DE CONTA INVÁLIDO \n" +
            "TIPOS DE CONTAS VÁLIDAS ===> Residencial ou Comercial"
        )
        print("\n=====================================================================\n")

    print("\n=====================================================================\n")   
    codigo = int(input("Digite um novo código ou digite zero para FINALIZAR O PROGRAMA ======>"))
    print("\n=====================================================================\n")

# Saída de Dados / Verificação de qual consumidor teve Menor Consumo de Kwh/mês
if totalConsumoComercial > totalConsumoResidencial:
    print("\n=====================================================================\n")
    print("O tipo de conta que teve menor consumo verificado foi a Residencial")
    print("\n=====================================================================\n")
elif totalConsumoComercial < totalConsumoResidencial:
    print("\n=====================================================================\n")
    print("O tipo de conta que teve menor consumo verificado foi a Comercial")
    print("\n=====================================================================\n")

# Saída de Dados/ Verificação de qual tipo de conta teve mais consumidor
if consumidoresResidencial > consumidoresComercial:
    print("\n=====================================================================\n")
    print("O tipo de conta que teve mais consumidores foi a Residencial ")
    print("\n=====================================================================\n")
elif consumidoresComercial > consumidoresResidencial:
    print("\n=====================================================================\n")
    print("O tipo de conta que teve mais consumidores foi a Comercial ")
    print("\n=====================================================================\n")
else:
    print("\n=====================================================================\n")
    print("Houve empate na quantidade de consumidores")
    print("\n=====================================================================\n")

#Calculo
totalGeral = totalConsumoComercial + totalConsumoResidencial
totalConsumidoires = consumidoresComercial + consumidoresResidencial
media = totalGeral / totalConsumidoires

# Saída De Dados / Média geral de Consumo
print("\n=====================================================================\n")
print("A média Geral de Consumo Foi de {}".format(media))
print("\n=====================================================================\n")
print("\n========================PROGRAMA FINALIZADO==========================\n")

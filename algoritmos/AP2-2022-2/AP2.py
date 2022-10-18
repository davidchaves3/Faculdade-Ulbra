totalConsumoResidencial = 0
totalConsumoComercial = 0
consumidoresResidencial = 0
consumidoresComercial = 0

# Entrada de Dados do preço do kwh para cada tipo de consumidor

precoResidencial = float(
    input("Digite o preço do Kw/h para consumidor Residencial: R$"))
precoComercial = float(
    input("Digite o preço do Kw/h para consumidor Comercial: R$"))

# Entrada de Dados/ código de Identificação

codigo = int(input("Digite o seu codigo de Identificação:"))
while codigo != 0:

    tipo = input("Qual o tipo de Conta[Residencial/Comercial]")
    if tipo == "Residencial":

        # Entrada da quantidade de kwh/mês
        contaResidencial = float(
            input("Digite a quantidade de kw/h gasto na sua residência  neste mês:"))

        # total de consumo de Kwh/mês da categoria Residencial
        totalConsumoResidencial = totalConsumoResidencial + contaResidencial
        totalPayResidencial = precoResidencial * \
            contaResidencial  # Valor que consumidor irá pagar
        consumidoresResidencial = consumidoresResidencial + 1

        # Saída de Dados
        print(
            "Código: {} \n Valor total  a pagar R${}".format(
                codigo, totalConsumoResidencial)
        )

    elif tipo == "Comercial":

        # Entrada da quantidade de kwh/mês
        contaComercial = float(
            input("Digite a quantidade de kw/h gasto no comercial este mês: "))
        # Calculos
        # total de consumo de Kwh/mês da categoria Comercial
        totalConsumoComercial = totalConsumoComercial + contaComercial
        totalPayComercial = precoComercial * \
            contaComercial  # Valor que consumidor irá pagar
        consumidoresComercial = consumidoresComercial + 1

        # Saída de Dados
        print(
            "Código: {} \n Valor total  a pagar R${}".format(
                codigo, totalConsumoComercial)
        )
    else:
        # Saída de Dados
        print(
            "TIPO DE CONTA INVÁLIDO \n" +
            "TIPOS DE CONTAS VÁLIDAS ===> Residencial ou Comercial"
        )
    codigo = int(input("Digite o seu codigo de Identificação:"))

# Saída de Dados / Verificação de qual consumidor teve Menor Consumo de Kwh/mês
if totalConsumoComercial > totalConsumoResidencial:
    print("O tipo de conta que teve menor consumo verificado foi a Residencial")
elif totalConsumoComercial < totalConsumoResidencial:
    print("O tipo de conta que teve menor consumo verificado foi a Comercial")

# Saída de Dados/ Verificação de qual tipo de conta teve mais consumidor
if consumidoresResidencial > consumidoresComercial:
    print("O tipo de conta que teve mais consumidores foi a Residencial ")
elif consumidoresComercial > consumidoresResidencial:
    print("O tipo de conta que teve mais consumidores foi a Comercial ")
else:
    print("Houve empate na quantidade de consumidores")

# Saída De Dados / Média geral de Consumo
print("A média Geral de Consumo Foi de {}".format((totalConsumoComercial +
      totalConsumoResidencial)/(consumidoresComercial + consumidoresResidencial)))

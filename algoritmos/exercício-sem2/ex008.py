ano = float(input('A quantos anos você fuma:'))
cigPordia = float(input('Quantos cigaros por dia:'))
valorCarteira = float(input('valor da carteira de cigarro R$'))

dias = ano * 365
totCig = cigPordia * dias
totCart = totCig/20

print('Qt. que fumou na vida:', totCig)
print('Dinheiro gasto:', totCart * valorCarteira)


custo = float(input('Qual o preço de custo do produto por unidade?'))
preco = float(input('Qual o preço para consumindor final?'))
unidade = float(input('Quantas unidades foram vendidas?'))

lucro_unidade = preco - custo
lucro = (lucro_unidade * unidade) - 500

print('Seu lucro foi de R$',lucro )

print('Bem-vindo a Loja do Guilherme Pena')
valor_unitario = float(input('Entre com o valor do produto: '))
quantidade_produto = float(input('Entre com a quantidade do produto: '))

#Calculando o valor total SEM DESCONTO
valor_total = valor_unitario * quantidade_produto

#Verificando condições

if valor_total >= 10000.00:
    valor_com_desconto = valor_total -(valor_total *0.11)
elif valor_total >= 6000.00 and valor_total < 10000.00:
    valor_com_desconto = valor_total -(valor_total *0.07)
elif valor_total >= 2500.00 and valor_total < 6000.00:
    valor_com_desconto = valor_total -(valor_total *0.04)
else:
    valor_com_desconto = valor_total

#Print dos valores de saida
print('O valor SEM desconto: R$', valor_total)
print(f'O valor COM desconto: R$ {valor_com_desconto:.2f}' )

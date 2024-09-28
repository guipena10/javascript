print("Bem vindo a Loja de Gelados do Guilherme")

# VALORES CUPUAÇU P=9 , M=14, G=18
# VALORES AÇAI P=11 , M=16, G=20
acumulador = 0

#Colocando estrutura de repetição

while True:
    valor_pedido = 0
    while True:
        sabor = input("Entre com o sabor desejado (CP/AC): ")
        if sabor in ('CP','cp','cP','Cp','AC','ac','Ac','aC'):
            break
        else:
            print('Sabor invalido. Tente novamente!\n')

    while True:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")
        if tamanho in ('P','M','G','p','m','g'):
            break
        else:
            print('Tamanho invalido. Tente novamente!\n')

    if sabor in ('CP','cp','cP','Cp'):
        nome_produto = 'Cupuaçu'
        if tamanho in ('p','P'):
            tamanho_produto = 'P'
            valor_pedido = 9.00
        elif tamanho in ('m','M'):
            tamanho_produto = 'M'
            valor_pedido = 14.00
        else:
            tamanho_produto = 'G'
            valor_pedido = 18.00

    if sabor in ('AC','ac','Ac','aC'):
        nome_produto = 'Açai'
        if tamanho in ('p','P'):
            tamanho_produto = 'P'
            valor_pedido = 11.00
        elif tamanho in ('m','M'):
            tamanho_produto = 'M'
            valor_pedido = 16.00
        else:
            tamanho_produto = 'G'
            valor_pedido = 20.00
    
    print(f'Você pediu um {nome_produto} no tamanho {tamanho_produto}: R$ {valor_pedido}')

#Somando os valores de mais de um pedido

    acumulador += valor_pedido



    pedido = input("\nDeseja mais alguma coisa? (S/N): ")
    if pedido in ('N','n'):
        break
    else:
        continue

print(f'O valor total a ser pago: R$ {acumulador}')
print("Bem vindo a Copiadora do Guilherme")

#Criando uma função com estrutura de repetição

def servico_extra():
    while True:
        global extra,valor_extra
        extra = input("Deseja adicionar algum serviço?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\n0 - Não desejo mais nada\n")
        try:
            extra = int(extra)
            if extra == 1:
                valor_extra = 15.00
                break
            elif extra == 2:
                valor_extra = 40.00
                break
            elif extra == 0:
                break
            else:
                print("Opção inválida. Favor selecionar novamente!\n")
        except:
            print('Valor não numérico digitado. Favor inserir um valor válido!\n')

def num_pagina():
    while True:
        global numero_paginas,pocentagem_de_desconto
        numero_paginas = input('Entre com o número de páginas: ')
        try:
            numero_paginas = int(numero_paginas)
            if numero_paginas < 20:
                pocentagem_de_desconto = 0
                break
            elif numero_paginas >= 20 and numero_paginas < 200:
                pocentagem_de_desconto = 0.15
                break
            elif numero_paginas >= 200 and numero_paginas < 2000:
                pocentagem_de_desconto = 0.20
                break
            elif numero_paginas >= 2000 and numero_paginas < 20000:
                pocentagem_de_desconto = 0.25
                break
            elif numero_paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.\nPor favor, entra com o número de páginas novamente.\n')
        except:
            print('Valor não numérico digitado. Favor inserir um valor válido!\n')


def escolha_servico():
    while True:
        global servico
        servico = input("Entre com o tipo de serviço desejado\nDIG - Digitação\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n")
        servico = servico.upper()
        if servico in ('DIG','ICO','IPB','FOT'):
            break
        else:
            print('Escolha invpalida, entre com o tipo de serviço novamente!')


escolha_servico()
num_pagina()
servico_extra()

if servico == 'DIG':
    valor_servico = 1.10
elif servico == 'ICO':
    valor_servico = 1.00
elif servico == 'IPB':
    valor_servico = 0.40
elif servico == 'FOT':
    valor_servico = 0.20

if extra == 1:
    valor_servico_extra = 15.00
elif extra == 2:
    valor_servico_extra = 40.00
elif extra == 0:
    valor_servico_extra = 0

#Fazendo a soma dos pedido + extra com apenas 2 casas decimais após o .
total = (valor_servico * numero_paginas) + valor_servico_extra
print(f"Total: R$ {total:.2f}")


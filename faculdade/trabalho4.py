print("Bem vindo a Livraria do Guilherme")

global lista_livro,id_global
id_global = 0
lista_livro = []

#Criação de uma função e estrutura de repetição para poder consultar os livros
def consultar_livro():
    while True:
        consulta = input("Escolha a opção desejada:\n1 - Consultar todos os livros\n2 - Consultar livro por ID\n3 - Consultar livro(s) por autor\n4 - Retornar\n")
        try:
            consulta = int(consulta)
            if consulta == 4:
                break
            elif consulta == 3:
                autor_selecionado = input("Digite nome do autor: ")
                for livro in range(len(lista_livro)):
                    if lista_livro[livro]['autor'] == autor_selecionado:
                        print(f"ID: {lista_livro[livro]['id']} | NOME: {lista_livro[livro]['nome']} | AUTOR: {lista_livro[livro]['autor']} | EDITORA: {lista_livro[livro]['editora']}\n")

            elif consulta == 2:
                id_selecionado = int(input("Digite o ID do livro: "))
                for livro in range(len(lista_livro)):
                    if lista_livro[livro]['id'] == id_selecionado:
                        print(f"ID: {lista_livro[livro]['id']} | NOME: {lista_livro[livro]['nome']} | AUTOR: {lista_livro[livro]['autor']} | EDITORA: {lista_livro[livro]['editora']}\n")

            elif consulta == 1:
                for livro in range(len(lista_livro)):
                    print(f"ID: {lista_livro[livro]['id']} | NOME: {lista_livro[livro]['nome']} | AUTOR: {lista_livro[livro]['autor']} | EDITORA: {lista_livro[livro]['editora']}\n")
            else:
                print("Opção inválida. Favor selecionar a opção desejada!\n")

        except:
            print('Valor não numérico digitado. Favor inserir um valor válido!\n')
#Criação de uma função e estrutura de repetição para poder remover os livros
def remover_livro():
    while True:
        id_invalido = True
        id_livro = int(input("Digite o ID do livro a ser removido: "))
        for livro in range(len(lista_livro)):         
            if lista_livro[livro]['id'] == id_livro:
                del(lista_livro[livro])
                id_invalido = False
                break

        if id_invalido == False:
            print("Livro removido com sucesso!\n")
            break
        elif id_invalido == True:
            print("ID inválido!\n")
#Criação de uma função e estrutura de repetição para poder cadastrar os livros
def cadastrar_livro(id):
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    dicionario = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    
#Adicionando o dicionario a lista

    lista_livro.append(dicionario)

#Estrutura de repetição para fazer o menu

while True:
    opcao_selecionada = input("Escolha a opção desejada:\n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n")
    try:
        opcao_selecionada = int(opcao_selecionada)
        if opcao_selecionada == 4:
            break
        elif opcao_selecionada == 3:
            remover_livro()
        elif opcao_selecionada == 2:
            consultar_livro()
        elif opcao_selecionada == 1:
            cadastrar_livro(id_global)
            id_global += 1
        else:
            print('Opção inválida!\n')
    
    except:
        print('Valor não numérico digitado. Favor inserir um valor válido!\n')
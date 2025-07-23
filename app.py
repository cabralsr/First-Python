import os

produtos = [

]

def exibir_nome_do_programa():
    print("""
░█████╗░░█████╗░███████╗███████╗███████╗███████╗  ░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝  ░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░  ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░  ░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║
╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
""")

def menu():
    print("""
        ===================
        1. 𝐶𝑎𝑑𝑎𝑠𝑡𝑟𝑎𝑟 𝑃𝑟𝑜𝑑𝑢𝑡𝑜
        2. 𝐿𝑖𝑠𝑡𝑎𝑟 𝑃𝑟𝑜𝑑𝑢𝑡𝑜𝑠
        3. 𝐸𝑑𝑖𝑡𝑎𝑟 𝑃𝑟𝑜𝑑𝑢𝑡𝑜
        4. 𝐸𝑥𝑐𝑙𝑢𝑖𝑟 𝑃𝑟𝑜𝑑𝑢𝑡𝑜
        5. 𝑆𝑎𝑖𝑟
        ===================
    """)

def finalizar_app():
    limpar_tela()
    print('Finalizando o app, atá a próxima!\n') 

def limpar_tela():
    os.system('cls')

def retornar_menu():
    input('Pressione ENTER para retornar ao menu...')
    main() 

def opcao_invalida():
    print('Opção inválida!\n')
    retornar_menu()

def cadastrar_produto():
    limpar_tela()

    print('CADASTRO DE PRODUTO\n')
    nome_do_produto = input('Digite o nome do produto: ')
    preco_do_produto = input('Digite o preço do produto: ')
    categoria_do_produto = input('Digite a categoria do produto: ')
    produto = {
        'nome': nome_do_produto,
        'preco': preco_do_produto,
        'categoria': categoria_do_produto
    }
    produtos.append(produto)
    print(f'O {nome_do_produto} foi cadastrado com sucesso!\n')

    retornar_menu()

def listar_produtos():
    limpar_tela()

    print('LISTA DE PRODUTOS\n')
    for produto in produtos:
        nome_do_produto = produto['nome']
        preco_do_produto = produto['preco']
        categoria_do_produto = produto['categoria']

        print(f'Nome: {nome_do_produto}')
        print(f'Preço: {preco_do_produto}')
        print(f'Categoria: {categoria_do_produto}\n')

    retornar_menu()

def editar_produto():
    pass

def excluir_produto():
    pass


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        if opcao_escolhida == 1:
            cadastrar_produto()
        elif opcao_escolhida == 2:
            listar_produtos()
        elif opcao_escolhida == 3:
            editar_produto()
        elif opcao_escolhida == 4:
            excluir_produto()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_tela()
    exibir_nome_do_programa()
    menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
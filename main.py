def menu():
    while True:
        print("\n1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Verificar Alertas")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print('cadastrando produto')
        elif escolha == '2':
            print('listando produtos')
        elif escolha == '3':
            id_produto = int(input("ID do produto: "))
            print('atualizando produto')
        elif escolha == '4':
            id_produto = int(input("ID do produto: "))
            print('deletando produto')
        elif escolha == '5':
            print('verificando alertas')
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
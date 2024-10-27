from crud_funcionarios import *

while True:
    op = menu()
    match(op):
        case 1:
            nome = input("Insira o nome do funcionário novo: ")
            cargo = input("Insira o cargo do funcionário novo: ")
            salario = input("Insira o salario do funcionário novo: ")
            status = True
            adicionar_funcionario(nome, cargo, salario, status)
        
        case 2:
            listar_funcionarios()
        
        case 3:
            atualizar_funcionario()
        case 4:
            listar_funcionarios_com_id()
            
            id = int(input("Insira o id do funcionário o qual deseja deletar: "))
            
            deletar_funcionario(id)
        case 5:
            print("Encerrando o sistema...")
            break    
        case _:
            print("Valor inválido!! Por favor, insira um valor de 1 á 5")
        
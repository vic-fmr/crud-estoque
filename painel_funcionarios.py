from crud_funcionarios import *
from time import sleep

while True:
    op = menu()
    match(op):
        case 1:
            limpar_terminal()
            
            nome = input("\nInsira o nome do funcionário novo: ")
            cargo = input("\nInsira o cargo: ")
            salario = float(input("\nInsira o salario do funcionário novo: R$"))
            
            while salario < 400: #Validação do salário inserido
                salario = float(input("Por favor, insira pelo menos R$ 400,00: R$"))
                
            status = True
            adicionar_funcionario(nome, cargo, salario, status)
            
            sleep(1.5)
        
        case 2:
            limpar_terminal()
            
            listar_funcionarios()
            
            sleep(1.5)
        case 3:
            limpar_terminal()
            atualizar_funcionario()
        case 4:
            limpar_terminal()
            listar_funcionarios_com_id()
            
            id = int(input("Insira o id do funcionário o qual deseja deletar: "))
            
            deletar_funcionario(id)
        case 5:
            limpar_terminal()
            print("Encerrando o sistema...")
            break    
        case _:
            print("Valor inválido!! Por favor, insira um valor de 1 á 5")
        
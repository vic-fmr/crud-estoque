import json
import os

funcionarios_json = os.path.join(os.path.dirname(__file__), 'funcionarios.json')

def carregar_funcionarios():
    if not os.path.exists(funcionarios_json):
        with open(funcionarios_json, 'w') as f:
            json.dump([], f, indent = 4)
        
    with open(funcionarios_json, 'r') as f:
        return json.load(f)
    
def adicionar_funcionario(nome, cargo, salario, status):
    funcionarios = carregar_funcionarios()

    # Garantir que seja cadastrado com um 'id' maior que o ultimo id cadastrado
    if funcionarios == []:
        id = 1
    else:
        for funcionario in funcionarios:
            if funcionario:
                id = funcionario['id'] + 1
    

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'status' : status})

    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    print(f"{nome} adicionado com sucesso!")
    
def listar_funcionarios():
    funcionarios = carregar_funcionarios()

    if(funcionarios):
        for funcionario in funcionarios:
            print(f"\nNome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            
            if funcionario['status'] == True:
                print("Status: ativo")
            else:
                print("Status: inativo")
    else:
        print("Sem funcionários cadastrados")
        
def listar_funcionarios_com_id():
    funcionarios = carregar_funcionarios()

    if(funcionarios):
        for funcionario in funcionarios:
            print(f"id: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            
            if funcionario['status'] == True:
                print("Status: ativo")
            else:
                print("Status: inativo")
    else:
        print("Sem funcionários cadastrados")

def atualizar_funcionario():
    funcionarios = carregar_funcionarios()
    listar_funcionarios_com_id()
        
    id = int(input("\nInsira o id correspondente ao funcionário a ser editado: "))
        
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            print(f"Dados atuais: ")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            
            if funcionario['status'] == True:
                print("Status: Ativo")
            else:
                print("Status: Inativo")
            
                
            dado_alterado = input("Digite o que deseja mudar: ").lower()
            
            novo_dado = input(f"Insira o novo {dado_alterado}: ")
                
                
            print(f"{funcionario['nome']} alterado com sucesso!")
                
            funcionario[f'{dado_alterado}'] = novo_dado
            
            
            break
    
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    
    print(f"Novos dados: ")
    listar_funcionarios()
    

def deletar_funcionario(id):
    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:  
        if funcionario['id'] == id:
            funcionarios.remove(funcionario)
            print(f"{funcionario['nome']} excluido com sucesso!")
            break

    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)

def menu():
    print("\n------------Gestão de Funcionários------------")
    print("\n1- Cadastrar funcionário.")
    print("\n2- Listar funcionários.")
    print("\n3- Atualizar dados de um funcionário.")
    print("\n4- Deletar funcionário.")
    print("\n5- Encerrar programa.")
    return int(input("\nInsira o código da sua atividade:"))




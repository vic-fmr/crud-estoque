import json
import os
from time import sleep

funcionarios_json = os.path.join(os.path.dirname(__file__), 'funcionarios.json')

def carregar_funcionarios():
    if not os.path.exists(funcionarios_json):
        with open(funcionarios_json, 'w') as f:
            json.dump([], f, indent = 4)
        
    with open(funcionarios_json, 'r') as f:
        return json.load(f)
    
def adicionar_funcionarios(nome, cargo, salario, status):
    funcionarios = carregar_funcionarios()

    # Garantir que seja cadastrado com um 'id' maior que o ultimo id cadastrado
    for funcionario in funcionarios:
        id = funcionario['id'] + 1

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'status' : status})

    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    print(f"{nome} adicionado com sucesso!")
    
def listar_funcionario():
    funcionarios = carregar_funcionarios()

    if(funcionarios):
        for funcionario in funcionarios:
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            
            if funcionario['status'] == True:
                print("Status: ativo")
            else:
                print("Status: inativo")
    else:
        print("Sem funcionários cadastrados")

def atualizar_funcionarios(id, nome, cargo, salario, status):
    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:
         
        if funcionario['id'] == id :
            funcionario['nome'] = nome
            funcionario['cargo'] = cargo
            funcionario['salario'] = salario
            funcionario['status'] = status

            print(f"{nome} alterado com sucesso!")
            break
    
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    
    

def deletar_usuario(id):
    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:  
        if funcionario['id'] == id:
            funcionarios.remove(funcionario)
            print(f"{funcionario['nome']} excluido com sucesso!")
            break

    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)






import tkinter
from tkinter import ttk, messagebox
from crud_funcionarios import *

import sv_ttk


def limpar_campos_entrada():
    entrada_nome.delete(0, tkinter.END)
    entrada_cargo.delete(0, tkinter.END)
    entrada_salario.delete(0, tkinter.END)

def capturar_campos_entrada():
    nome = entrada_nome.get()
    cargo = entrada_cargo.get()
    salario = float(entrada_salario.get())
    
    return nome, cargo, salario

def atualizar_JSON(funcionarios):
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    

def listar_funcionarios_na_interface():
    funcionarios = carregar_funcionarios()
    lista_funcionarios.delete(*lista_funcionarios.get_children())
    
    funcionarios_formatado = [list(funcionario.values()) for funcionario in funcionarios]

    for cabecalho in colunas:
        lista_funcionarios.heading(cabecalho, text=cabecalho)
        
        if cabecalho == "Id":
            lista_funcionarios.column(cabecalho, anchor="center", width=30)
        else:
            lista_funcionarios.column(cabecalho, anchor="center")
    
    for dado_funcionario in funcionarios_formatado:

        dado_funcionario[4] = "Ativo" if dado_funcionario[4] else "Inativo"
        
        dado_funcionario.append("Editar")
        dado_funcionario.append("Deletar")
        
        lista_funcionarios.insert('', tkinter.END, values=dado_funcionario)

def adicionar_funcionario_na_lista():
    funcionarios = carregar_funcionarios()
    
    nome, cargo, salario = capturar_campos_entrada()

    # Garantir que seja cadastrado com um 'id' maior que o ultimo id cadastrado
    if funcionarios == []:
        id = 1
    else:
        for funcionario in funcionarios:
            id = funcionario['id'] + 1
    

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'status' : True})

    atualizar_JSON(funcionarios)
    
    listar_funcionarios_na_interface()
    limpar_campos_entrada()


# Função para manipular ações na coluna de botões
def editar_funcionario(event):
    item_id = lista_funcionarios.identify_row(event.y)
    col = lista_funcionarios.identify_column(event.x)
    values = lista_funcionarios.item(item_id, "values")
    
    if col == "#6":
        limpar_campos_entrada()
    
        entrada_nome.insert(0, values[1])
        entrada_cargo.insert(0, values[2])
        entrada_salario.insert(0, values[3])
        
        capturar_botao.config(command=lambda: atualizar_funcionario_interface(int(values[0])), text="Atualizar Cadastro")
        

    elif col == "#7":  # Coluna "Delete"
        confirm = messagebox.askyesno("Confirmar", f"Tem certeza de que deseja {values[1]}?")
        
        if confirm:
            deletar_funcionario(int(values[0]))
            listar_funcionarios_na_interface()

def atualizar_funcionario_interface(id):
    funcionarios = carregar_funcionarios()
    
    nome, cargo, salario = capturar_campos_entrada()
    
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            
            funcionario['nome'] = nome
            funcionario['cargo'] = cargo
            funcionario['salario'] = salario
            
    atualizar_JSON(funcionarios)
        
    limpar_campos_entrada() 
    listar_funcionarios_na_interface()
    
    capturar_botao.config(text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista)
    

#Aqui começa a interface:
root = tkinter.Tk()
sv_ttk.set_theme("dark")


root.title("Gerenciar Funcionário")

frame_lista_funcionarios = ttk.Frame(root)
frame_lista_funcionarios.grid(row=0, column=1, pady=10)

frame_entrada_dados = ttk.LabelFrame(root, text="Cadastro e Atualização de Funcionários")
frame_entrada_dados.grid(row=0, column=0, padx= 5)


label_nome = ttk.Label(frame_entrada_dados, text="Nome do Funcionário")
entrada_nome = ttk.Entry(frame_entrada_dados)
label_nome.pack(pady=(20, 0))
entrada_nome.pack(padx=10)

label_cargo = ttk.Label(frame_entrada_dados, text="Cargo")
entrada_cargo = ttk.Entry(frame_entrada_dados)
label_cargo.pack(pady=(20, 0))
entrada_cargo.pack()

label_salario = ttk.Label(frame_entrada_dados, text="Salário")
entrada_salario = ttk.Entry(frame_entrada_dados)
label_salario.pack(pady=(20,0))
entrada_salario.pack(pady=(0, 20))

capturar_botao = ttk.Button(frame_entrada_dados, text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista, style="Accent.TButton", width=20)
capturar_botao.pack(pady=10)



lista_funcionarios_scroll = ttk.Scrollbar(frame_lista_funcionarios)
lista_funcionarios_scroll.pack(side="right", fill="y")


colunas = ("Id", "Nome", "Cargo", "Salário", "Status", "====================" , "======================")
lista_funcionarios = ttk.Treeview(frame_lista_funcionarios, show="headings", yscrollcommand=lista_funcionarios_scroll.set, columns=colunas)
lista_funcionarios.pack()


lista_funcionarios_scroll.config(command=lista_funcionarios.yview)
lista_funcionarios.bind("<ButtonRelease-1>", editar_funcionario)



listar_funcionarios_na_interface()



root.mainloop()
import tkinter
from tkinter import ttk, messagebox
from crud_funcionarios import *

import sv_ttk

def listar_funcionarios_na_interface():
    funcionarios = carregar_funcionarios()
    lista_funcionarios.delete(*lista_funcionarios.get_children())
    
    funcionarios_formatado = [list(funcionario.values()) for funcionario in funcionarios]

    for cabecalho in colunas:
        lista_funcionarios.heading(cabecalho, text=cabecalho)
        
        if cabecalho == "Id":
            lista_funcionarios.column(cabecalho, anchor="center", width=30)
            
        lista_funcionarios.column(cabecalho, anchor="center")
    
    for dado_funcionario in funcionarios_formatado:

        dado_funcionario[4] = "Ativo" if dado_funcionario[4] else "Inativo"
        
        dado_funcionario.append("Editar")
        dado_funcionario.append("Deletar")
        
        lista_funcionarios.insert('', tkinter.END, values=dado_funcionario)

def adicionar_funcionario_na_lista():
    funcionarios = carregar_funcionarios()

    nome = entrada_nome.get()
    cargo = entrada_cargo.get()
    salario = entrada_salario.get()
    # Garantir que seja cadastrado com um 'id' maior que o ultimo id cadastrado
    if funcionarios == []:
        id = 1
    else:
        for funcionario in funcionarios:
            id = funcionario['id'] + 1
    

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'status' : True})

    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    
    listar_funcionarios_na_interface()
    
    entrada_nome.delete(0, tkinter.END)
    entrada_cargo.delete(0, tkinter.END)
    entrada_salario.delete(0, tkinter.END)


# Função para manipular ações na coluna de botões
def editar_funcionario(event):
    item_id = lista_funcionarios.identify_row(event.y)
    col = lista_funcionarios.identify_column(event.x)
    values = lista_funcionarios.item(item_id, "values")
    
   

    if col == "#6":  # Coluna "Update"

        
    
        # Insere o valor de "Nome" no Entry correspondente
        entrada_nome.delete(0, tkinter.END)
        entrada_nome.insert(0, values[1])
        entrada_cargo.delete(0, tkinter.END)
        entrada_cargo.insert(0, values[2])
        entrada_salario.delete(0, tkinter.END)
        entrada_salario.insert(0, values[3])# Coluna Nome
        
        # Botão de confirmação para o update
        capturar_botao.config(command=lambda: atualizar_funcionario_interface(int(values[0])), text="Atualizar Cadastro")
        

    elif col == "#7":  # Coluna "Delete"
        confirm = messagebox.askyesno("Confirmar", "Tem certeza de que deseja deletar este item?")
        if confirm:
            deletar_funcionario(int(values[0]))
            listar_funcionarios_na_interface()

def atualizar_funcionario_interface(id):
    funcionarios = carregar_funcionarios()
    
    nome = entrada_nome.get()
    cargo = entrada_cargo.get()
    salario = entrada_salario.get()
    
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            funcionario['nome'] = nome
            funcionario['cargo'] = cargo
            funcionario['salario'] = salario
            
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
        
    entrada_nome.delete(0, tkinter.END)
    entrada_cargo.delete(0, tkinter.END)
    entrada_salario.delete(0, tkinter.END)

        
    listar_funcionarios_na_interface()
    
    capturar_botao.config(text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista)
    

root = tkinter.Tk()
sv_ttk.set_theme("dark")

frame_lista_funcionarios = ttk.Frame(root)
frame_lista_funcionarios.grid(row=0, column=1, pady=10)

frame_entrada_dados = ttk.LabelFrame(root, text="Cadastro de Funcionários")
frame_entrada_dados.grid(row=0, column=0)

label_nome = ttk.Label(frame_entrada_dados, text="Nome do Funcionário")
entrada_nome = ttk.Entry(frame_entrada_dados)

label_cargo = ttk.Label(frame_entrada_dados, text="Cargo")
entrada_cargo = ttk.Entry(frame_entrada_dados)

label_salario = ttk.Label(frame_entrada_dados, text="Salário")
entrada_salario = ttk.Entry(frame_entrada_dados)

capturar_botao = ttk.Button(frame_entrada_dados, text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista)

label_nome.pack()
entrada_nome.pack()
label_cargo.pack()
entrada_cargo.pack()
label_salario.pack()
entrada_salario.pack()
capturar_botao.pack()




lista_funcionarios_scroll = ttk.Scrollbar(frame_lista_funcionarios)
lista_funcionarios_scroll.pack(side="right", fill="y")

colunas = ("Id", "Nome", "Cargo", "Salário", "Status", "====================" , "======================")
lista_funcionarios = ttk.Treeview(frame_lista_funcionarios, show="headings",
                                  yscrollcommand=lista_funcionarios_scroll.set, columns=colunas)


lista_funcionarios.bind("<ButtonRelease-1>", editar_funcionario)

lista_funcionarios.pack()
lista_funcionarios_scroll.config(command=lista_funcionarios.yview)
listar_funcionarios_na_interface()



root.mainloop()
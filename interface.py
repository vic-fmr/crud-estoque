import tkinter
from tkinter import ttk, messagebox
from crud_funcionarios import *

import sv_ttk


def limpar_campos_entrada():
    entrada_nome.delete(0, tkinter.END)
    entrada_cargo.delete(0, tkinter.END)
    entrada_salario.delete(0, tkinter.END)
    entrada_setor.delete(0, tkinter.END)

def capturar_campos_entrada():
    nome = entrada_nome.get()
    cargo = entrada_cargo.get()
    salario = float(entrada_salario.get())
    setor = entrada_setor.get()    
    return nome, cargo, salario, setor

def atualizar_JSON(funcionarios):
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    

def listar_funcionarios_na_interface():
    funcionarios = carregar_funcionarios()
    lista_funcionarios.delete(*lista_funcionarios.get_children())
    
    funcionarios_formatado = [list(funcionario.values()) for funcionario in funcionarios]

    for cabecalho in colunas:
        lista_funcionarios.heading(cabecalho, text=cabecalho)
        
        match(cabecalho):
            case "Id":
                lista_funcionarios.column(cabecalho, anchor="center", width=30)
            case "Nome":
                lista_funcionarios.column(cabecalho, anchor="center", width=250)
            case "Salário":
                lista_funcionarios.column(cabecalho, anchor="center", width=50)
            case "Cargo":
                lista_funcionarios.column(cabecalho, anchor="center", width=250)
            case "Setor":
                lista_funcionarios.column(cabecalho, anchor="center", width=100)
            case _:
                lista_funcionarios.column(cabecalho, anchor="center", width=50)

                

    
    for dado_funcionario in funcionarios_formatado:
        
        dado_funcionario.append("Editar")
        dado_funcionario.append("Deletar")
        
        lista_funcionarios.insert('', tkinter.END, values=dado_funcionario)

def adicionar_funcionario_na_lista():
    funcionarios = carregar_funcionarios()
    
    nome, cargo, salario, setor = capturar_campos_entrada()

    if funcionarios == []:
        id = 1
    else:
        for funcionario in funcionarios:
            id = funcionario['id'] + 1
    

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'setor' : setor})

    atualizar_JSON(funcionarios)
    
    listar_funcionarios_na_interface()
    limpar_campos_entrada()


def editar_funcionario(event):
    item_id = lista_funcionarios.identify_row(event.y)
    col = lista_funcionarios.identify_column(event.x)
    values = lista_funcionarios.item(item_id, "values")
    
    if col == "#6":
        limpar_campos_entrada()
    
        entrada_nome.insert(0, values[1])
        entrada_cargo.insert(0, values[2])
        entrada_salario.insert(0, values[3])
        entrada_setor.insert(0, values[4])
        
        capturar_botao.config(command=lambda: atualizar_funcionario_interface(int(values[0])), text="Atualizar Cadastro")
        

    elif col == "#7":  # Coluna "Delete"
        confirm = messagebox.askyesno("Confirmar", f"Tem certeza de que deseja deletar {values[1]}?")
        
        if confirm:
            deletar_funcionario(int(values[0]))
            listar_funcionarios_na_interface()

def buscar_funcionario_na_interface():
    id = int(entrada_id_busca.get())
    
    
    funcionarios = carregar_funcionarios()
    
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            lista_funcionarios.delete(*lista_funcionarios.get_children())

            dados_funcionario = []
            for dado_funcionario in funcionario:
                dados_funcionario.append(funcionario[dado_funcionario])
                
            dados_funcionario.append("Editar")
            dados_funcionario.append("Deletar")
        
            
            lista_funcionarios.insert('', tkinter.END, values=dados_funcionario)
            return
        
        
            
            

def atualizar_funcionario_interface(id):
    funcionarios = carregar_funcionarios()
    
    nome, cargo, salario, setor = capturar_campos_entrada()
    
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            
            funcionario['nome'] = nome
            funcionario['cargo'] = cargo
            funcionario['salario'] = salario
            funcionario['setor'] = setor
            
    atualizar_JSON(funcionarios)
        
    limpar_campos_entrada() 
    listar_funcionarios_na_interface()
    
    capturar_botao.config(text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista)
    

#Aqui começa a interface:
root = tkinter.Tk()
sv_ttk.set_theme("dark")
root.geometry("1280x720")


root.title("Gerenciar Funcionário")

frame_lista_funcionarios = ttk.Frame(root)
frame_lista_funcionarios.pack(side="right", fill=tkinter.BOTH, pady=20)

frame_entrada_dados = ttk.LabelFrame(root, text="Gerenciamento de Funcionários")
frame_entrada_dados.pack(fill="x", pady=20, padx=20)


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

label_setor = ttk.Label(frame_entrada_dados, text="Setor")
entrada_setor = ttk.Entry(frame_entrada_dados)
label_setor.pack()
entrada_setor.pack(pady=(0, 20))


capturar_botao = ttk.Button(frame_entrada_dados, text="Cadastrar Funcionário", command=adicionar_funcionario_na_lista, style="Accent.TButton", width=20)
capturar_botao.pack(pady=10)

label_buscar_funcionario = ttk.Label(frame_entrada_dados, text="Buscar funcionário por id")
entrada_id_busca = ttk.Entry(frame_entrada_dados, width=5)
label_buscar_funcionario.pack(pady=(40,0))
entrada_id_busca.pack(pady=(0,10))

capturar_botao_busca = ttk.Button(frame_entrada_dados, text="Buscar Funcionário", command=buscar_funcionario_na_interface, style="Accent.TButton",width=20)
capturar_botao_busca.pack(pady=(10,10))


lista_funcionarios_scroll = ttk.Scrollbar(frame_lista_funcionarios)
lista_funcionarios_scroll.pack(side="right", fill="y")


colunas = ("Id", "Nome", "Cargo", "Salário", "Setor", "====================" , "======================")
lista_funcionarios = ttk.Treeview(frame_lista_funcionarios, show="headings", yscrollcommand=lista_funcionarios_scroll.set, columns=colunas)
lista_funcionarios.pack(fill=tkinter.BOTH, expand=True)


lista_funcionarios_scroll.config(command=lista_funcionarios.yview)
lista_funcionarios.bind("<ButtonRelease-1>", editar_funcionario)



listar_funcionarios_na_interface()



root.mainloop()

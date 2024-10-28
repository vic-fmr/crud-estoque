import tkinter
from tkinter import ttk
from crud_funcionarios import *

import sv_ttk

def listar_funcionarios_na_interface():
    funcionarios = carregar_funcionarios()
    
    funcionarios_formatado = [list(funcionario.values()) for funcionario in funcionarios]

    for cabecalho in colunas:
        lista_funcionarios.heading(cabecalho, text=cabecalho)
        lista_funcionarios.column(cabecalho, anchor="center")
    
    for dado_funcionario in funcionarios_formatado:

        dado_funcionario[4] = "Ativo" if dado_funcionario[4] else "Inativo"
        
        lista_funcionarios.insert('', tkinter.END, values=dado_funcionario)

root = tkinter.Tk()
sv_ttk.set_theme("dark")

frame_lista_funcionarios = ttk.Frame(root)
frame_lista_funcionarios.grid(row=0, column=0, pady=10)

lista_funcionarios_scroll = ttk.Scrollbar(frame_lista_funcionarios)
lista_funcionarios_scroll.pack(side="right", fill="y")

colunas = ("Id", "Nome", "Cargo", "Salário", "Status")
lista_funcionarios = ttk.Treeview(frame_lista_funcionarios, show="headings",
                                  yscrollcommand=lista_funcionarios_scroll.set, columns=colunas, height=15)
lista_funcionarios.pack()
lista_funcionarios_scroll.config(command=lista_funcionarios.yview)
listar_funcionarios_na_interface()

root.mainloop()
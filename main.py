import tkinter as tk
from time import sleep
import os

# FUNÇÕES
def buscar_descricao():
    url = url_entry.get()
    if 'https://' not in url:
        tk.messagebox.showerror(title='Erro', message='Insira um Link para iniciar uma busca.')
    else:
        # Código de busca da descrição aqui
        descricao = 'Descrição do produto'
        descricao_entry.delete(0, tk.END)
        descricao_entry.insert(0, descricao)

def cadastrar_produto():
    nome = nome_entry.get()
    gtin = gtin_entry.get()
    peso = peso_entry.get()
    preco = preco_entry.get()
    descricao = descricao_entry.get()
    # Código de cadastro do produto aqui
    print(f'Produto {nome} cadastrado com sucesso!')
    print(f'GTIN: {gtin}')
    print(f'Peso: {peso}')
    print(f'Preço: {preco}')
    print(f'Descrição: {descricao}')

def novo_produto():
    nome_entry.delete(0, tk.END)
    gtin_entry.delete(0, tk.END)
    peso_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)

# JANELA PRINCIPAL
janela = tk.Tk()
janela.title('Cadastro')
janela.geometry('500x400')

# WIDGETS
titulo_label = tk.Label(janela, text='Hora de cadastrar os produtos!')
titulo_label.pack()

nome_label = tk.Label(janela, text='Nome')
nome_label.pack()
nome_entry = tk.Entry(janela,width=50)
nome_entry.pack()

gtin_label = tk.Label(janela, text='GTIN')
gtin_label.pack()
gtin_entry = tk.Entry(janela,width=50)
gtin_entry.pack()

peso_label = tk.Label(janela, text='Peso')
peso_label.pack()
peso_entry = tk.Entry(janela,width=50) 
peso_entry.pack()

preco_label = tk.Label(janela, text='Preço')
preco_label.pack()
preco_entry = tk.Entry(janela,width=50)
preco_entry.pack()

url_label = tk.Label(janela, text='Link/Url')
url_label.pack()
url_entry = tk.Entry(janela,width=50)
url_entry.pack()

buscar_button = tk.Button(janela, text='Buscar', command=buscar_descricao)
buscar_button.pack()

descricao_label = tk.Label(janela, text='Janela de Saída - Editar Descrição')
descricao_label.pack()
descricao_entry = tk.Text(janela, width=60, height=22)
descricao_entry.pack()

novo_button = tk.Button(janela, text='Novo\nProduto', width=10, height=2, command=novo_produto)
novo_button.pack(side=tk.LEFT, padx=10)

finalizar_button = tk.Button(janela, text='Finalizar\n Programa', width=10, height=2, command=janela.quit)
finalizar_button.pack(side=tk.RIGHT, padx=10)

cadastro_button = tk.Button(janela, text='Cadastrar\nProduto', width=10, height=2, command=cadastrar_produto)
cadastro_button.pack(side=tk.LEFT, padx=10)

# LOOP PRINCIPAL
janela.mainloop()

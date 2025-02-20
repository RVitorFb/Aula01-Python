import tkinter as tk
from tkinter import messagebox

# Função para realizar uma saudação ao usuário
def saudacao():
    nome = entry_nome.get()
    if nome:
        messagebox.showinfo("Saudação", f"Olá, {nome}! Seja bem-vindo(a)!")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome.")

# Função para somar dois números fornecidos pelo usuário
def somar_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        soma = num1 + num2
        messagebox.showinfo("Resultado da Soma", f"A soma de {num1} e {num2} é {soma}")
    except ValueError:
        messagebox.showwarning("Aviso", "Por favor, insira números válidos.")

# Função para realizar uma contagem regressiva a partir de um número fornecido pelo usuário
def contagem_regressiva():
    try:
        numero = int(entry_contagem.get())
        contagem = ""
        while numero >= 0:
            contagem += str(numero) + "\n"
            numero -= 1
        messagebox.showinfo("Contagem Regressiva", contagem)
    except ValueError:
        messagebox.showwarning("Aviso", "Por favor, insira um número válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Programa com Interface Gráfica")

# Configuração do estilo da interface
root.configure(bg='#f0f0f0')

# Estilos de fonte
font_label = ('Arial', 12, 'bold')
font_entry = ('Arial', 12)
font_button = ('Arial', 12, 'bold')

# Criação dos elementos da interface
label_nome = tk.Label(root, text="Nome:", font=font_label, bg='#f0f0f0')
label_nome.pack(pady=5)

entry_nome = tk.Entry(root, font=font_entry)
entry_nome.pack(pady=5)

button_saudacao = tk.Button(root, text="Saudação", font=font_button, command=saudacao, bg='#4CAF50', fg='white')
button_saudacao.pack(pady=5)

label_num1 = tk.Label(root, text="Primeiro Número:", font=font_label, bg='#f0f0f0')
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root, font=font_entry)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Segundo Número:", font=font_label, bg='#f0f0f0')
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root, font=font_entry)
entry_num2.pack(pady=5)

button_somar = tk.Button(root, text="Somar Números", font=font_button, command=somar_numeros, bg='#4CAF50', fg='white')
button_somar.pack(pady=10)

label_contagem = tk.Label(root, text="Número para Contagem Regressiva:", font=font_label, bg='#f0f0f0')
label_contagem.pack(pady=5)

entry_contagem = tk.Entry(root, font=font_entry)
entry_contagem.pack(pady=5)

button_contagem = tk.Button(root, text="Iniciar Contagem Regressiva", font=font_button, command=contagem_regressiva, bg='#4CAF50', fg='white')
button_contagem.pack(pady=10)

# Execução da janela principal
root.mainloop()
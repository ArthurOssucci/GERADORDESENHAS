import random
import string
import tkinter as tk

def gerar_senha():
    comprimento = comprimento_var.get()
    if not comprimento:
        resultado_label.config(text="Digite um comprimento válido.")
        return

    comprimento = int(comprimento)
    usar_maiusculas = maiusculas_var.get()
    usar_minusculas = minusculas_var.get()
    usar_digitos = digitos_var.get()
    usar_especiais = especiais_var.get()

    caracteres = ''

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        resultado_label.config(text="Escolha pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    resultado_label.config(text="Sua senha é: " + senha)

app = tk.Tk()
app.title("Gerador de Senha")

app.configure(bg="white")

comprimento_var = tk.StringVar()
maiusculas_var = tk.BooleanVar()
minusculas_var = tk.BooleanVar()
digitos_var = tk.BooleanVar()
especiais_var = tk.BooleanVar()

comprimento_label = tk.Label(app, text="Comprimento da senha:", bg="white", font=("Arial", 14))
comprimento_entry = tk.Entry(app, textvariable=comprimento_var)
maiusculas_checkbox = tk.Checkbutton(app, text="Incluir letras maiúsculas", variable=maiusculas_var, bg="white", font=("Arial", 12))
minusculas_checkbox = tk.Checkbutton(app, text="Incluir letras minúsculas", variable=minusculas_var, bg="white", font=("Arial", 12))
digitos_checkbox = tk.Checkbutton(app, text="Incluir dígitos", variable=digitos_var, bg="white", font=("Arial", 12))
especiais_checkbox = tk.Checkbutton(app, text="Incluir caracteres especiais", variable=especiais_var, bg="white", font=("Arial", 12))
gerar_button = tk.Button(app, text="Gerar Senha", command=gerar_senha, bg="white", font=("Arial", 12))
resultado_label = tk.Label(app, text="", bg="white", font=("Arial", 12))

comprimento_label.pack()
comprimento_entry.pack()
maiusculas_checkbox.pack()
minusculas_checkbox.pack()
digitos_checkbox.pack()
especiais_checkbox.pack()
gerar_button.pack()
resultado_label.pack()

app.mainloop()

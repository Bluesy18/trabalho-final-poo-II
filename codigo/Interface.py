import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

from Usuario import Usuario
from Login import LoginStorage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Usuários")
        self.login_storage = LoginStorage()

        # Tela inicial
        tk.Label(root, text="Bem-vindo! Escolha uma opção:").pack(pady=10)

        self.register_button = tk.Button(root, text="Cadastrar", command=self.tela_cadastro)
        self.register_button.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.tela_login)
        self.login_button.pack(pady=5)

    def tela_cadastro(self):
        self.limpar_tela()

        tk.Label(self.root, text="Cadastro de Usuário").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Nome de Usuário:").grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Senha:").grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_usuario).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).grid(row=4, column=0, columnspan=2)

    def tela_login(self):
        self.limpar_tela()

        tk.Label(self.root, text="Login de Usuário").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Nome de Usuário:").grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Senha:").grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Entrar", command=self.login_usuario).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).grid(row=4, column=0, columnspan=2)

    def cadastrar_usuario(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        usuarios = self.login_storage.load_logins()

        if username in usuarios:
            messagebox.showerror("Erro", "Nome de usuário já cadastrado.")
            return

        novo_usuario = Usuario(username, password)
        usuarios[username] = novo_usuario.to_dict()

        self.login_storage.save_login(usuarios)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

        self.tela_inicial()

    def login_usuario(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        usuarios = self.login_storage.load_logins()

        if username in usuarios and usuarios[username]["password"] == password:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
            self.tela_autenticado(username)
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

    def tela_autenticado(self, username):
        self.limpar_tela()

        tk.Label(self.root, text=f"Usuário {username} autenticado com sucesso!").pack(pady=20)
        tk.Button(self.root, text="Sair", command=self.tela_inicial).pack(pady=10)

    def tela_inicial(self):
        self.limpar_tela()
        self.__init__(self.root)

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Configuração inicial do Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import random

from Usuario import Usuario
from Login import LoginStorage, RentStorage
from Aluguel import Rent

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Usuários")
        self.login_storage = LoginStorage()
        self.rent_storage = RentStorage()

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
        tk.Button(self.root, text="Alugar Filme", command=lambda: self.alugar(username)).pack(pady=10)
        tk.Button(self.root, text="Ver Meus Aluguéis", command=lambda: self.visualizar_alugueis(username)).pack(pady=10)

    def alugar(self, username):
        self.limpar_tela()

        tk.Label(self.root, text="Digite o nome do filme para alugar:").pack(pady=10)
        self.movie_entry = tk.Entry(self.root)
        self.movie_entry.pack(pady=5)

        tk.Button(self.root, text="Buscar Filme", command=lambda: self.buscar_filme(username)).pack(pady=10)

    def buscar_filme(self, username):
        movie_name = self.movie_entry.get().strip()
        if not movie_name:
            messagebox.showerror("Erro", "O nome do filme é obrigatório.")
            return

        filme = Rent.rent_movie(movie_name)
        if "error" in filme:
            messagebox.showerror("Erro", filme["error"])
        else:
            self.confirmar_aluguel(filme, username)

    def confirmar_aluguel(self, filme, username):
        self.limpar_tela()
        tk.Label(self.root, text=f"Filme: {filme['Title']} ({filme['Year']})").pack(pady=5)
        tk.Label(self.root, text=f"Gênero: {filme['Genre']}").pack(pady=5)
        tk.Label(self.root, text=f"Preço por dia: R${filme['PricePerDay']}").pack(pady=5)

        tk.Label(self.root, text="Por quantos dias deseja alugar?").pack(pady=5)
        dias_entry = tk.Entry(self.root)
        dias_entry.pack(pady=5)

        def finalizar():
            try:
                dias = int(dias_entry.get())
                if dias <= 0:
                    messagebox.showerror("Erro", "O número de dias deve ser maior que 0.")
                    return
                
                total = dias * filme['PricePerDay']
                aluguel = {
                    "filme": filme['Title'],
                    "data": datetime.now().strftime("%Y-%m-%d"),
                    "dias": dias,
                    "total": total
                }
                self.rent_storage.save_rent(username, aluguel)
                messagebox.showinfo("Sucesso", f"Aluguel concluído! Total: R${total:.2f}")
                self.tela_autenticado(username)
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido para dias.")

        tk.Button(self.root, text="Finalizar Aluguel", command=finalizar).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=lambda: self.tela_autenticado(username)).pack(pady=20)


        

    def visualizar_alugueis(self, username):
        self.limpar_tela()

        alugueis = self.rent_storage.load_rents(username)

        if not alugueis:
            tk.Label(self.root, text="Você ainda não fez nenhum aluguel.").pack(pady=20)
        else:
            tk.Label(self.root, text="Seus Aluguéis:").pack(pady=20)
            for aluguel in alugueis:
                tk.Label(self.root, text=f"Filme: {aluguel['filme']} | Data: {aluguel['data']} | Dias: {aluguel['dias']} | Total: R${aluguel['total']:.2f}").pack(pady=5)

        tk.Button(self.root, text="Voltar", command=lambda: self.tela_autenticado(username)).pack(pady=20)


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
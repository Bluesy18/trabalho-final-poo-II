from Login import LoginStorage
import tkinter as tk
from tkinter import messagebox




class AuthUI:
    def _init_(self):
        self.login_storage = LoginStorage()
        self.users = self.login_storage.load_logins()

        self.root = tk.Tk()
        self.root.title("Login/Registro")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.title = tk.Label(self.frame, text="Bem-vindo", font=("Arial", 16))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_label = tk.Label(self.frame, text="Usuário:")
        self.username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1)

        self.password_label = tk.Label(self.frame, text="Senha:")
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1)

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, pady=10)

        self.register_button = tk.Button(self.frame, text="Registrar", command=self.register)
        self.register_button.grid(row=3, column=1, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.root.destroy()
            #WeatherAppUI().run()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Erro", "Usuário e senha são obrigatórios!")
            return

        if username in self.users:
            messagebox.showerror("Erro", "Usuário já registrado!")
            return

        self.users[username] = password
        self.login_storage.save_login(self.users)
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
from Usuario import Usuario
from getpass import getpass

class Locadora():
  def __init__(self, estoque):
    self.estoque = estoque
    self.usuarios = []
    self.algueis = []
    self.usuario_atual = None

  def registrar_usuario(self):
    print("=== REGISTRO DE USUÁRIO ===")

    while True:
      nome = input("Digite seu nome: ")
      
      if (nome.isalpha() == True):
        break
      
      else:
        print("Nome inválido, tente novamente.")

    usuario = Usuario(nome)

    while True:
      cpf = input("Digite seu CPF: ")
      if(usuario.validar_cpf(cpf, self.usuarios)):
        usuario.set_cpf(cpf)
        usuario.info.append(cpf)
        break
      print("CPF inválido, tente novamente.")

    while True:
      senha = input("Digite sua senha: ")
      if(usuario.definir_senha(senha, usuario)):
        usuario.set_senha(senha)
        break
      print("Senha inválida, tente novamente.")

    self.usuarios.append(usuario)

  def realizar_login(self):
    logado = False
    print("=== LOGIN ===")
    while True:
      cpfLogin = input("Digite seu CPF: ")
      senhaLogin = getpass("Digite sua senha: ")
      for i in self.usuarios:
        if(cpfLogin == i.get_cpf() and senhaLogin == i.get_senha()):
          self.usuario_atual = i
          logado = True
          print("Login feito com sucesso.")
          break
      if (logado):
        break
      print("Informações inválidas, tente novamente.")
      


  
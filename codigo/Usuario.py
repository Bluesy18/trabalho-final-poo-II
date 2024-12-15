import re

class Usuario ():
  def __init__(self, nome):
    self.nome = nome
    self.cpf = None
    self.senha = None

  def validar_cpf(self, cpf, usuarios):
    for _ in usuarios:
      if (cpf in _.get_cpf()):
        return False

    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return False

    cpf = cpf.replace('.', '').replace('-', '')

    if cpf == cpf[0] * len(cpf):
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0

    return cpf[-2:] == f"{digito1}{digito2}"
    

  def definir_senha(self, senha, usuario):
    for i in usuario.get_info():
      if(i.upper() in senha.upper()):
        return False
    
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, senha))

  def get_nome(self):
    return self.nome

  def get_cpf(self):
    return self.cpf

  def get_senha(self):
    return self.senha

  
  def set_cpf(self, cpf):
    self.cpf = cpf

  def set_senha(self, senha):
    self.senha = senha

class Filme ():
  def __init__(self, titulo, genero, qtd_estoque):
    self.titulo = titulo
    self.genero = genero
    self.qtd_estoque = qtd_estoque

  def __str__(self):
    return f"\Título: {self.titulo}\nGênero: {self.genero}\nQuantidade em estoque: {self.qtd_estoque}"

  def atualizar_estoque(self, qtd):
    self.qtd_estoque -= qtd

  def get_titulo(self):
    return self.titulo

  def get_genero(self):
    return self.genero

  def get_qtd_estoque(self):
    return self.qtd_estoque
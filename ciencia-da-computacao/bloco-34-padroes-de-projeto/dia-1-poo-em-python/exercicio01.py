class television:
  def __init__(self, tamanho):
    self.volume = 50
    self.canal = 1
    self.tamanho = tamanho
    self.ligada = False

  def aumentar_volume(self):
    self.volume = 99 if self.volume > 100 else self.volume + 1
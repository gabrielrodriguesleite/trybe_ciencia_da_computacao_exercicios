class television:
  def __init__(self, tamanho):
    self.volume = 50
    self.canal = 1
    self.tamanho = tamanho
    self.ligada = False

  def aumentar_volume(self):
    self.volume = 99 if self.volume > 100 else self.volume + 1

  def diminuir_volume(self):
    self.volume = 0 if self.volume < 0 else self.volume - 1

  def modificar_canal(self, canal):
    if 1 > canal > 99:
      raise ValueError
    self.canal = canal

  def ligar_desligar(self):
    self.ligada = not self.ligada
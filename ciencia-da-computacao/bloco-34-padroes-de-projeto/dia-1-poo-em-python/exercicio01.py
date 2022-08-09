import pytest


class television:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        self.__volume = 99 if self.__volume > 100 else self.__volume + 1

    def diminuir_volume(self):
        self.__volume = 0 if self.__volume < 0 else self.__volume - 1

    def modificar_canal(self, canal):
        if canal > 99 or canal < 1:
            raise ValueError("canal fora de alcance")

        self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada

    @property
    def volume(self):
        return self.__volume

    @property
    def canal(self):
        return self.__canal

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def ligada(self):
        return self.__ligada


def test_television_created():
    tv = television(50)
    assert tv.tamanho == 50
    assert tv.volume == 50
    assert tv.canal == 1
    assert tv.ligada is False


def test_television_ligar_desligar():
    tv = television(50)
    tv.ligar_desligar()
    assert tv.tamanho == 50
    assert tv.volume == 50
    assert tv.canal == 1
    assert tv.ligada is True
    tv.ligar_desligar()
    assert tv.tamanho == 50
    assert tv.volume == 50
    assert tv.canal == 1
    assert tv.ligada is False


def test_television_volume():
    tv = television(32)
    for i in range(10):
        tv.aumentar_volume()

    assert tv.volume == 60

    for i in range(20):
        tv.diminuir_volume()

    assert tv.volume == 40

    for i in range(100):
        tv.diminuir_volume()

    assert tv.volume == 0

    for i in range(150):
        tv.aumentar_volume()

    assert tv.volume == 99


def test_television_canal():
    tv = television(14)
    with pytest.raises(ValueError, match="canal fora de alcance"):
        tv.modificar_canal(0)

    with pytest.raises(ValueError, match="canal fora de alcance"):
        tv.modificar_canal(100)

    tv.modificar_canal(1)
    assert tv.canal == 1

    tv.modificar_canal(99)
    assert tv.canal == 99

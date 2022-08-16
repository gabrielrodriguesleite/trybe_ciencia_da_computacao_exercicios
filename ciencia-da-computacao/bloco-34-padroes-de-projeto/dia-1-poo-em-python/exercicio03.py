import pytest
from abc import ABC


class geometryAbs(ABC):
    def area(self):
        pass

    def perimetro(self):
        pass


class quadrado(geometryAbs):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado * self.lado


def test_quadrado_area():
    assert quadrado(4).area() == 16
    assert quadrado(11).area() == 121


if __name__ == '__main__':
    print(quadrado(4).area())

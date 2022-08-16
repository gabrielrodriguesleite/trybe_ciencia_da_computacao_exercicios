import pytest
from abc import ABC


class geometryAbs(ABC):
    @classmethod
    def area(self):
        pass

    @classmethod
    def perimetro(self):
        pass


class quadrado(geometryAbs):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4


def test_quadrado_area():
    assert quadrado(4).area() == 16
    assert quadrado(11).area() == 121
    
def test_quadrado_perimetro():
    assert quadrado(5).perimetro() == 20
    assert quadrado(11).perimetro() == 44


class retangulo(geometryAbs):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return self.base * 2 + self.altura * 2
        

def test_retangulo_area():
    assert retangulo(4, 5).area() == 20
    assert retangulo(11, 12).area() == 132

if __name__ == '__main__':
    print(quadrado(4).area())

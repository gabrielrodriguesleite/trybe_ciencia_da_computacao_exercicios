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

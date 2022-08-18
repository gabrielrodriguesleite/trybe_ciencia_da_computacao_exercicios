from abc import ABC, abstractmethod


class EstrategiaDeImposto(ABC):
    @abstractmethod
    def calcular(cls, valor):
        raise NotImplementedError


class ISS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.1


class ICMS(EstrategiaDeImposto):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.06


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, imposto):
        if imposto == 'ISS':
            return self.__calcular_iss()
        elif imposto == 'ICMS':
            return self.__calcular_icms()
        elif imposto == 'PIS':
            return self.__calcular_pis()
        elif imposto == 'COFINS':
            return self.__calcular_cofins()

    def __calcular_iss(self):
        return self.valor * 0.1

    def __calcular_icms(self):
        return self.valor * 0.06

    def __calcular_pis(self):
        return self.valor * 0.0065

    def __calcular_cofins(self):
        return self.valor * 0.03


orcamento = Orcamento(1000)
print(f"ISS: {orcamento.calcular_imposto('ISS')}")
print(f"ICMS: {orcamento.calcular_imposto('ICMS')}")
print(f"PIS: {orcamento.calcular_imposto('PIS')}")
print(f"COFINS: {orcamento.calcular_imposto('COFINS')}")

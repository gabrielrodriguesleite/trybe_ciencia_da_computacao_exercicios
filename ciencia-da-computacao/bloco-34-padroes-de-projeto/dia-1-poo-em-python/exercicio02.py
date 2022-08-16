from re import I


import pytest

class Estatistica:
    def media(self, lista):
        """Calculo de média aritimética dos números de uma lista

        Args:
            lista (array de números): um array de números

        Returns:
            float: a soma de todos os números dividido pela quantidade
        """
        sum = 0
        for i in lista:
            sum += i
        return sum / len(lista)

    def mediana(self):
        pass

    def moda(self):
        pass

def test_estatistica_media():
    assert Estatistica().media([1,2,3]) == 2.0
    assert Estatistica().media([5,4,9]) == 6.0
    
def test_estatistica_mediana():
    assert Estatistica().mediana([1,2,3]) == 2
    assert Estatistica().mediana([32,6,4,9]) == 5.0
    

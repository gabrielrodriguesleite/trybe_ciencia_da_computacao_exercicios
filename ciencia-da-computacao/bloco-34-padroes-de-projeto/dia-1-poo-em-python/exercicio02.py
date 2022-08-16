from re import I


import pytest

class Estatistica:
    def media(self, lista):
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
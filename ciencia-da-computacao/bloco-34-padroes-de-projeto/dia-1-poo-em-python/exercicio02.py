from re import I


import pytest

class Estatistica:
    def media(self, lista):
        sum = 0
        for i in lista:
            sum += i
        return sum

    def mediana(self):
        pass

    def moda(self):
        pass

def test_estatistica_media():
    assert Estatistica().media([1,2,3]) == 6
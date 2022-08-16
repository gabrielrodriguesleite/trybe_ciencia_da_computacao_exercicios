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

    def mediana(self, lista):
        lista.sort()
        if len(lista) % 2 == 0:
            return (lista[int(len(lista)/2)] + lista[int(len(lista)/2)+1])/2

        return lista[int(len(lista)/2)]

    def moda(self):
        pass

def test_estatistica_media():
    assert Estatistica().media([1,2,3]) == 2.0
    assert Estatistica().media([5,4,9]) == 6.0
    
def test_estatistica_mediana():
    assert Estatistica().mediana([1,2,3]) == 2
    assert Estatistica().mediana([31,6,4,9]) == 20.0
    

if __name__ == "__main__":
    print(Estatistica().mediana([31,6,4,9]))
    print(Estatistica().mediana([1,2,3]))
    
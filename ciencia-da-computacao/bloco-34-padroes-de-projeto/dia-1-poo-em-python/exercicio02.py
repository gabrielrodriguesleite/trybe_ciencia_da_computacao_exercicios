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
        """Cálculo da mediana

        Args:
            lista (array de números): um array de números

        Returns:
            número: O valor central de um conjunto ordenado ou a média dos 2 valores centrais
        """
        lista.sort()
        if len(lista) % 2 == 0:
            return (lista[int(len(lista)/2)] + lista[int(len(lista)/2)+1])/2

        return lista[int(len(lista)/2)]

    def moda(self, lista):
        """Cálculo de moda

        Args:
            lista (array de números): um array de números
            
        Returns:
            número: O número que aparece com mais frequência em um conjunto de dados
        """
        lista.sort()
        m = {}
        for i in lista:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        o = 0
        for j in m:
            if m[j] > o:
                o = m[j]
        return [f for f in m if m[f] == o][0]

def test_estatistica_media():
    assert Estatistica().media([1,2,3]) == 2.0
    assert Estatistica().media([5,4,9]) == 6.0
    
def test_estatistica_mediana():
    assert Estatistica().mediana([1,2,3]) == 2
    assert Estatistica().mediana([31,6,4,9]) == 20.0
    
def test_estatistica_moda():
    assert Estatistica().moda([1,1,2,3,3,3,3,4,4,5,5,5]) == 3
    assert Estatistica().moda([155,13,22,33,35,35,34,4,446,56,56,35]) == 35
    

if __name__ == "__main__":
    # print(Estatistica().mediana([31,6,4,9]))
    # print(Estatistica().mediana([1,2,3]))
    print(Estatistica().moda([1,1,2,3,3,3,3,4,4,5,5,5]))
    
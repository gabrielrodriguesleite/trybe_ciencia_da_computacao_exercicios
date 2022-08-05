def fator(num):
    for i in range(num):
        num += i

    return num


def test_fator():
    assert fator(5) == 15

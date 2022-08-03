# TDD em python - Testes

Dos mesmos autores do J-unity do java:

###### REFERÊNIAS
https://docs.pytest.org/en/7.1.x/

## pyteste

Instalação do pytest


```sh
python3 -m pip install pytest
python3 -m pytest --version
```

## Exemplo do pytest

```py
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
    # assert 1 == 1 # saída ''(nada)
    # assert 1 == 0 # saída AssertionError
```
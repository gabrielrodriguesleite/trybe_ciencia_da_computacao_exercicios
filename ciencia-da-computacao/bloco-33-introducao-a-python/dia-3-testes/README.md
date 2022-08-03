# TDD em python - Testes

Para executar todos os testes execute na pasta do ambiente o seguinte comando

```sh
pytest
```

Se não rodar por conta dos imports tente

```sh
python3 -m pytest
```

A tag -v aumenta a verbosidade do resultado do teste

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

# Ambiente virtual e dev requirementes

```sh
python3 -m venv .venv && source .venv/bin/activate

```

./dev-requirementes.txt
```txt
pytest
```

## Fixture (lê-se fik-chur)

```py
import pytest

@pytest.fixture # decorador
def stock():
    return [{"id":1},{"id":2},{"id":3}]

# as fixtures devem ser colocadas em um arquivo separado e importadas

def test_a_minha_funcao(stock):
    report = minha_funcao(stock)
    assert "dados retornados da minha função" in report
```
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

# Ambiente virtual e dev requirementes

```sh
python3 -m venv .venv && source .venv/bin/activate

```
## Instalar as dependencias de projeto python

Projeto possuindo um arquivo requirements.txt
./dev-requirements.txt

```sh
pip install -r dev-requirements.txt
```

## Executar os tests com pytest
Para executar todos os testes execute na pasta do ambiente o seguinte comando

```sh
pytest
```

Se não rodar por conta dos imports tente

```sh
python3 -m pytest
```

A tag -v aumenta a verbosidade do resultado do teste

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

## Teste de excessão

```py
## Esse é o exemplo bugado do Eli
import pytest

from pasta.arquivo import funcao_que_da_erro

def teste_se_teve_erro():
    with pytest.raises(ValueError, match="mensagem do erro"):
      # contexto onde se espera a excessão
      funcao_que_da_erro("um parametro que causa erro")

## ASSIM ESTÁ NA DOCUMENTAÇÃO https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=raises#pytest.raises

with pytest.raises(ValueError) as exc_info:
    raise ValueError("value must be 42")
assert exc_info.type is ValueError
assert exc_info.value.args[0] == "value must be 42"

```

## Teste com data

```py
import pytest
from datetime import date

print(date.today().isoformat()) # '2022-08-03'

def exemplo_recover_expired_drugs(drugs_recover)
    today = date.today().isoformat()
    return [
      drug for drug in drugs_recover() if drug["data_de_validade"] < today
    ]
```

# Exercícios do dia

🚀 Exercício 1: Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções:

- Números divisíveis por 3 deve aparecer como "Fizz" ao invés do número;
- Números divisíveis por 5 devem aparecer como "Buzz" ao invés do número;
- Números divisíveis por 3 e 5 devem aparecer como "FizzBuzz" ao invés do número.

Exemplo: 3 -> [1, 2, "Fizz"].


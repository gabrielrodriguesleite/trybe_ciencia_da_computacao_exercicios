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

🚀 **Exercício 1:** Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções:

- Números divisíveis por 3 deve aparecer como "Fizz" ao invés do número;
- Números divisíveis por 5 devem aparecer como "Buzz" ao invés do número;
- Números divisíveis por 3 e 5 devem aparecer como "FizzBuzz" ao invés do número.

Exemplo: 3 -> [1, 2, "Fizz"].

**Exercício 2:** Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira, a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase, e os dígitos 1 e 0 não estão associados a nenhuma letra.
Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

```
Letras  ->  Número
ABC     ->  2
DEF     ->  3
GHI     ->  4
JKL     ->  5
MNO     ->  6
PQRS    ->  7
TUV     ->  8
WXYZ    ->  9
```
Exemplo de entrada:
```
1-HOME-SWEET-HOME
MY-MISERABLE-JOB
```
Saídas correspondentes:
```
1-4663-79338-4663
69-647372253-562
```
    Curiosidade: A frase "The quick brown fox jumps over the lazy dog" é um pantograma (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.

Verifique casos como entrada maior que 30 caracteres, vazia e com caracteres inválidos.

Para executar o teste rode
```sh
python3 -m pytest -v ciencia-da-computacao/bloco-33-introducao-a-python/dia-3-testes/exercicio-02.py
```

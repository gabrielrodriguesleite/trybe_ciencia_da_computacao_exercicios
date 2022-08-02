# trybe_ciencia_da_computacao_exercicios
Repositorio com os exercicios de ciencias da computação da Trybe

## Criação de ambiente  virtual no python

```sh
sudo apt install python3-venv
# o ambiente criado tem o nome de ambiente mas é comum chamar .venv
python3 -m venv .ambiente
source .ambiente/bin/activate
```

## Para ativar o linter no vscode:

Ctrl+Shift+P → "Select Linter" → flake8

## Para formatar o arquivo com black:

```sh
python3 -m black nomes_dos_arquivos.py
```
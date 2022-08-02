# Dia 2 entrada e saída de dados

## Aula ao vivo

### JSON com arquivo de dados de jogos

### Print

```py

# print sem quebra de linha
print("Na mesma", end=" ")
print("Linha") # saída "Na mesma Linha

# formatar precisão
print(f"3 / 4 = {3 / 4:.2f}") # saída 3 / 4 = 0.75

# centralizar
item = '(G)'
print(f"{item:.^20}") # saida '........(G).........'
```

### Escrevendo um arquivo

```py
with open('arquivo.txt', mode='w'):
    file.write("primeira linha\n")

    LINHAS = ['item1\n', 'item2\n', 'item3\n', 'item4\n']
    file.writelines(LINHAS)

    print("segunda linha", file=file)
```

### Desempacotando valores

```py
a, b = "cd"
print(a) # saida c
print(b) # saida d

h, *t = (1, 2, 3)
print(h) # saida 1
print(t) # saida [2, 3]
```

### Erros na saída padrão

```py
import sys

err = "Arquivo não encontrado"
print(f"Erro: {err}", file=sys.stderr)
```

### Explorando o limite do sistema de abrir arquivos

```py
arquivos = []
for index in range(10240):
    arquivos.append(open(f"arquivo{index}.txt", "w"))
```
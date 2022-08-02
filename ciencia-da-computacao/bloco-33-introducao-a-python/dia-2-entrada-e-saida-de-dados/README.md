# Dia 2 entrada e saída de dados

## Aula ao vivo

### JSON com arquivo de dados de jogos

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

### Explorando o limite do sistema de abrir arquivos

```py
arquivos = []
for index in range(10240):
    arquivos.append(open(f"arquivo{index}.txt", "w"))
```
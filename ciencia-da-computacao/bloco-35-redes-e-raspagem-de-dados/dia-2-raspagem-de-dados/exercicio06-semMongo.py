import json


FILE = (
    "ciencia-da-computacao/bloco-35-redes-e-"
    "raspagem-de-dados/dia-2-raspagem-de-dados/books.json")
with open(FILE) as file:
    print(json.load(file))

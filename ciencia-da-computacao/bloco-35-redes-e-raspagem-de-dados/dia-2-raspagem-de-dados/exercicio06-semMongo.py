import json


FILE = (
    "ciencia-da-computacao/bloco-35-redes-e-"
    "raspagem-de-dados/dia-2-raspagem-de-dados/books.json")
with open(FILE) as file:
    books = json.load(file)

category = "Java"

for book in books:
    if category in book["categories"]:
        print(book["title"])

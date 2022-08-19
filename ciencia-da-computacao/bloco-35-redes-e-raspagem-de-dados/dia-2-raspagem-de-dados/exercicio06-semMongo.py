import json


def list_book_category(category):

    FILE = (
        "ciencia-da-computacao/bloco-35-redes-e-"
        "raspagem-de-dados/dia-2-raspagem-de-dados/books.json")
    with open(FILE) as file:
        books = json.load(file)

    # category = "Java"

    for book in books:
        if category in book["categories"]:
            print(book["title"])


if __name__ == "__main__":
    print("Digite uma categoria:")
    list_book_category(input())

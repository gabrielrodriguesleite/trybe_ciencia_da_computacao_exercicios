import json


def rank_published_books():

    FILE = (
        "ciencia-da-computacao/bloco-35-redes-e-"
        "raspagem-de-dados/dia-2-raspagem-de-dados/books.json")
    with open(FILE) as file:
        books = json.load(file)

    rank = {}
    for book in books:
        if book["status"] == "PUBLISH":
            for cat in book["categories"]:
                if cat not in rank:
                    rank[cat] = 1
                else:
                    rank[cat] += 1

    # sorted usa a key como referencia pra ordenação
    # lambda recebe item como parametro x e retorna o 2° valor
    # que nesse caso é a quantidade, dict transforma tuplas em dicionário
    print(dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)))


if __name__ == "__main__":
    rank_published_books()

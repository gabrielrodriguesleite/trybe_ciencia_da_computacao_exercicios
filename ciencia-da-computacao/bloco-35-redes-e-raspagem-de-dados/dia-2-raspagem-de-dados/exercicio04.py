import requests
from parsel import Selector


def crawl(url):
    return requests.get(
        url,
        headers={"User-agent": "Mozilla", "Accept": "text/html"})


if __name__ == "__main__":
    data = crawl(
        "http://books.toscrape.com/catalogue/"
        "the-grand-design_405/index.html"
    ).text
    sel = Selector(data)
    title = sel.css("div.col-sm-6 > h1::text").get()
    price = ""
    description = ""
    image_url = ""
    print(title, price, description, image_url)

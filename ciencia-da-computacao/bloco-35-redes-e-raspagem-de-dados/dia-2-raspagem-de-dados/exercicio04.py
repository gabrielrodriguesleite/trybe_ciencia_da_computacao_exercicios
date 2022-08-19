import requests
from parsel import Selector


def crawl(url):
    return requests.get(
        url,
        headers={"User-agent": "Mozilla", "Accept": "text/html"})


if __name__ == "__main__":
    BASE_URL = (
        "http://books.toscrape.com/catalogue/"
        "the-grand-design_405/index.html"
    )
    data = crawl(BASE_URL).text
    sel = Selector(data)
    title = sel.css("div.col-sm-6 > h1::text").get()
    price = sel.css("p.price_color::text").re_first(r"\d+\.\d{2}")
    description = sel.css("article > p::text").get()
    description = description[:-len(" ...more")]
    image_url = BASE_URL + sel.css("div.thumbnail img::attr(src)").get()
    # exercicio 05
    quantity = sel.css("p.instock.availability::text").re_first(r"\d")
    print(title, price, description, image_url, quantity, sep=",")

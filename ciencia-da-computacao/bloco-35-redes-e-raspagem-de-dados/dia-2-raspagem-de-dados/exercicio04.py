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
    price = sel.css("p.price_color::text").re_first(r"\d+\.\d{2}")
    description = sel.css("article > p::text").get()
    description = description[:-len(" ...more")]
    image_url = ""
    print(title, price, description, image_url, sep=",")

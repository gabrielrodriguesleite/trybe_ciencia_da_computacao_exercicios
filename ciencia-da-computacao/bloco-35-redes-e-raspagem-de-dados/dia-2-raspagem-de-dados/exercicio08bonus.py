import requests
from parsel import Selector


def crawl(url) -> requests:
    return requests.get(
        url,
        headers={"User-agent": "Mozilla", "Accept": "text/html"})


def get_flags_urls() -> list:
    URL = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
    galeryResponse = crawl(URL)
    if galeryResponse.status_code == 200:
        sel = Selector(galeryResponse.text)
        flagssrc = sel.css("a.image > img::attr(src)").getall()
        flags = [f"https:{f}" for f in flagssrc]
        # print(flags[0])
        return flags


def save_image_from_url(url):
    # https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    r = requests.get(url, stream=True)
    with open(url.split('/')[-1], mode="wb") as file:
        for chunk in r:
            file.write(chunk)


def main():
    # print(crawl(get_flags_urls()[0]).)
    # save_image_from_url(get_flags_urls()[0])
    for i in get_flags_urls():
        save_image_from_url(i)


if __name__ == "__main__":
    main()

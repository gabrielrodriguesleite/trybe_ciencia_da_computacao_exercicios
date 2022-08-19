import requests


def crawl(url):
    return requests.get(
        url,
        headers={"User-agent": "Mozilla", "Accept": "text/html"})
